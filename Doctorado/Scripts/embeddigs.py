# Imports
import sys
sys.path.append('../Scripts')
import baseline_model as b

import pandas as pd, numpy as np
import gensim
import gensim.downloader as api
import matplotlib.pyplot as plt
import pandas as pd
import spacy
import string

from gensim.models.word2vec import Word2Vec
from gensim.models import word2vec
from gensim.models import KeyedVectors
from sklearn import metrics


class Embeddings:
    def __init__(self, embedding_path, is_w2v_format, data_train, data_test, 
                 x_label_column, y_label_column, ai_model, target_names):
        self.embedding_path = embedding_path
        self.is_w2v_format = is_w2v_format
        self.data_train = data_train
        self.data_test = data_test
        self.x_label_column = x_label_column
        self.y_label_column = y_label_column
        self.ai_model = ai_model
        self.target_names = target_names

    def sentence_vector(self, sentence, word_vector):
        vector_size = word_vector.vector_size
        wv_res = np.zeros(vector_size)
        ctr = 1
        
        for word in sentence:
            if word in word_vector:
                ctr += 1
                wv_res += word_vector[word]
        
        wv_res = wv_res / ctr
        return wv_res
    

    def tokenize(self, sentence):
        tokens = sentence.split()
        return tokens
        
        
    def word_embedding(self):
        # Load model
        print('Loading embeddings')
        if self.is_w2v_format:
            word_vectors = KeyedVectors.load_word2vec_format(self.embedding_path)
        else:
            word_vectors = KeyedVectors.load(self.embedding_path)
        
        # Creating tokens of text data
        print('Sentence to tokens')
        train, test = self.data_train, self.data_test
        train['tokens'] = train[self.x_label_column].apply(self.tokenize)
        test['tokens'] = test[self.x_label_column].apply(self.tokenize)

        # Creating vectors of tokens
        print('Tokens to word vectors')
        train['vector'] = train['tokens'].apply(self.sentence_vector, word_vector=word_vectors)
        test['vector'] = test['tokens'].apply(self.sentence_vector, word_vector=word_vectors)

        # Creating lists of data for models
        print('Transforming train and test data')
        X_train = train['vector'].to_list()
        y_train = train[self.y_label_column].to_list()
        X_test = test['vector'].to_list()
        y_test = test[self.y_label_column].to_list()

        # Train model
        print('Training model')
        model = self.ai_model
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Results
        clf_report = metrics.classification_report(y_test, 
                                        y_pred, 
                                        target_names=self.target_names)
        confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
        accuracy = metrics.accuracy_score(y_test, y_pred)

        print(clf_report)

        return model, [clf_report, confusion_matrix, accuracy]
