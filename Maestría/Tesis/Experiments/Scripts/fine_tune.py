'''Imports'''
import torch
from tqdm.notebook import tqdm
from transformers import BertTokenizer, RobertaTokenizer, RobertaModel
from torch.utils.data import TensorDataset
from transformers import BertForSequenceClassification, RobertaForSequenceClassification
import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split

# Metrics
from sklearn.metrics import f1_score, precision_score, recall_score, \
                            classification_report

# Data loaders
from torch.utils.data import DataLoader, RandomSampler, SequentialSampler

# Optimizer and scheduler
from transformers import AdamW, get_linear_schedule_with_warmup

'''Fine tune class'''
class FineTune:
    def __init__(self, model, model_name, data_train, data_test, text_column, 
                max_len, device, batch_size, tokenizer, optimizer, 
                num_warmup_steps, epochs, seed):
        self.model = model
        self.model_name = model_name
        self.data_train = data_train
        self.data_test = data_test
        self.text_column = text_column
        self.max_len = max_len
        self.device = device
        self.batch_size = batch_size
        self.tokenizer = tokenizer
        self.optimizer = optimizer
        self.num_warmup_steps = num_warmup_steps
        self.epochs = epochs
        self.seed = seed

    def encode_data(self):
        # Encode data train
        encoded_data_train = self.tokenizer.batch_encode_plus(
            self.data_train[self.text_column].values,
            add_special_tokens = True,
            return_attention_mask = True,
            pad_to_max_length = True,
            max_length = self.max_len,
            return_tensors = 'pt')

        # Encode data test
        encoded_data_test = self.tokenizer.batch_encode_plus(
            self.data_test[self.text_column].values,
            add_special_tokens = True,
            return_attention_mask = True,
            pad_to_max_length = True,
            max_length = self.max_len,
            return_tensors = 'pt')
        return encoded_data_train, encoded_data_test
        
    def create_input_ids(self):
        encoded_data_train, encoded_data_test = self.encode_data()
        # Train input ids
        input_ids_train = encoded_data_train['input_ids']
        attention_masks_train = encoded_data_train['attention_mask']
        labels_train = torch.tensor(self.data_train.tags.values)

        # Test input ids
        input_ids_test = encoded_data_test['input_ids']
        attention_masks_test = encoded_data_test['attention_mask']
        labels_test = torch.tensor(self.data_test.tags.values)

        return input_ids_train, attention_masks_train, labels_train, input_ids_test, attention_masks_test, labels_test
    
    def train_test_datasets(self):
        input_ids_train, attention_masks_train, labels_train, input_ids_test, attention_masks_test, labels_test = self.create_input_ids()
        
        # Train and test datasets
        dataset_train = TensorDataset(input_ids_train, attention_masks_train, 
                                    labels_train)
        dataset_test = TensorDataset(input_ids_test, attention_masks_test, 
                                    labels_test)
        
        return dataset_train, dataset_test

    def create_dataloaders_and_scheduler(self):
        dataset_train, dataset_test = self.train_test_datasets()
        dataloader_train = DataLoader(dataset_train,
                                    sampler = RandomSampler(dataset_train),
                                    batch_size = self.batch_size)

        dataloader_test = DataLoader(dataset_test,
                                    sampler = RandomSampler(dataset_test),
                                    batch_size = self.batch_size)
        
        scheduler = get_linear_schedule_with_warmup(self.optimizer,
                        num_warmup_steps = self.num_warmup_steps,
                        num_training_steps = len(dataloader_train) * self.epochs)
        
        return dataloader_train, dataloader_test, scheduler

    def training_loop(self):
        dataloader_train, dataloader_test, scheduler = self.create_dataloaders_and_scheduler()
        random.seed(self.seed)
        np.random.seed(self.seed)
        torch.manual_seed(self.seed)
        torch.cuda.manual_seed_all(self.seed)

        self.model.to(self.device)

        for epoch in tqdm(range(1, self.epochs + 1)):
            self.model.train()
            loss_train_total = 0
            progress_bar = tqdm(dataloader_train, desc = 'Epoch {:1d}'.format(epoch), 
                                leave = False, disable = False)
        
            for batch in progress_bar:
                self.model.zero_grad()
                batch = tuple(b.to(self.device) for b in batch)
                inputs = {'input_ids':      batch[0],
                            'attention_mask': batch[1],
                            'labels':         batch[2]}       

                outputs = self.model(**inputs)
                loss = outputs[0]
                loss_train_total += loss.item()
                loss.backward()
                torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1.0)

                self.optimizer.step()
                scheduler.step()
                
                progress_bar.set_postfix({'training_loss': '{:.3f}'.format(loss.item() / len(batch))})
            
            
            torch.save(self.model.state_dict(), 
                        f'/content/model/finetuned_{self.model_name}_epoch_{epoch}.model')
                
            tqdm.write(f'\nEpoch {epoch}')
            loss_train_avg = loss_train_total / len(dataloader_train)            
            tqdm.write(f'Training loss: {loss_train_avg}')

            def evaluate(dataloader):
                self.model.eval()
                
                loss_val_total = 0
                predictions, true_vals = [], []
                
                for batch in dataloader:        
                    batch = tuple(b.to(self.device) for b in batch)
                    inputs = {'input_ids':      batch[0],
                            'attention_mask': batch[1],
                            'labels':         batch[2]}

                    with torch.no_grad():        
                        outputs = self.model(**inputs)
                        
                    loss = outputs[0]
                    logits = outputs[1]
                    loss_val_total += loss.item()

                    logits = logits.detach().cpu().numpy()
                    label_ids = inputs['labels'].cpu().numpy()
                    predictions.append(logits)
                    true_vals.append(label_ids)
                
                loss_val_avg = loss_val_total / len(dataloader) 
                predictions = np.concatenate(predictions, axis = 0)
                true_vals = np.concatenate(true_vals, axis = 0)
                        
                return loss_val_avg, predictions, true_vals

            def scorer(preds, labels):
                preds_flat = np.argmax(preds, axis = 1).flatten()
                labels_flat = labels.flatten()
                
                report = classification_report(labels_flat, preds_flat)
                f1 = f1_score(labels_flat, preds_flat, average = 'weighted')
                precision = precision_score(labels_flat, preds_flat, average = 'weighted')
                recall = recall_score(labels_flat, preds_flat, average = 'weighted')
                
                print(report)

                return report, f1, precision, recall
            
            val_loss, predictions, true_vals = evaluate(dataloader_test)
            report, f1, precision, recall = scorer(predictions, true_vals)
    