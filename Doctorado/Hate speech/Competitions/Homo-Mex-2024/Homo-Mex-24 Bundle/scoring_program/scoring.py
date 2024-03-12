import json
import os
import numpy as np
from sklearn.metrics import f1_score, precision_score, recall_score, hamming_loss, accuracy_score
import pandas as pd
import zipfile

reference_dir = os.path.join('/app/input/', 'ref')
prediction_dir = os.path.join('/app/input/', 'res')
score_dir = '/app/output/'

print('Reading prediction')

tasks = ['task_1', 'task_2', 'task_3']  

for task_number, task in range(tasks):
    # Verifying if the participant uploaded a file for each task
    if os.path.exists(prediction_dir, f'{task}_predictions.csv'):
        print(f'Predictions for task {task_number + 1} finded')
        
        ## task_X_true.csv is the name of the file in the reference dataset ZIP
        truth = pd.read_csv(os.path.join(reference_dir, f'{task}_true.csv'))

        ## track_X_predictions.csv is the name of the file submitted by the participants
        prediction = pd.read_csv(os.path.join(prediction_dir, f'{task}_predictions.csv'))

        print('Verifying the IDs order')
        if truth['sub_id'] == prediction['sub_id']:

            print('Extracting your predictions...')
            if task_number in [0,2]:
                truth = list(truth['label'])
                prediction = list(prediction['label'])
            
            else:
                truth = truth.iloc[:, 2:7].values
                prediction = prediction.iloc[:, 2:7].values

            print('Scoring...')
            f1 = f1_score(truth, prediction, average='macro')
            precision = precision_score(truth, prediction, average='macro')
            recall = recall_score(truth, prediction, average='macro')
            hamming = hamming_loss(truth, prediction)
            exact_match = accuracy_score(truth, prediction, normalize=True, sample_weight=None)

            scores = {
                'f1-score' : f1,
                'precision' : precision,
                'recall' : recall,
                'hamming' : hamming,
                'EMR' : exact_match
            }

            print('Saving scores...')

            with open(os.path.join(score_dir, 'scores.json'), 'w') as score_file:
                score_file.write(json.dumps(scores))
        
        else:
            print('The IDs are not in the same order, please verify your file')


