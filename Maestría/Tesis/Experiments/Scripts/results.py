'''Imports'''
# DataManipulation class
from data_manipulation import DataManipulation
# import data_manipulation as DataManipulation

# DataManipulation class
from feature_extraction import FeatureExtraction
# import feature_extraction as FeatureExtraction

# DataFrames manipulation library
import pandas as pd

# Plot libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Library to save models
import joblib

# This library offers comprehensive mathematical functions
import numpy as np

# Metrics
from sklearn.metrics import classification_report, confusion_matrix

'''Results class'''
class Results:
    def __init__(self, data_manipulation, machine_learning, validation_results, model_names,
                models_path, vectorizers_path, vectorizer):
        self.data_manipulation = data_manipulation
        self.machine_learning = machine_learning
        self.validation_results = validation_results
        self.model_names = model_names
        self.models_path = models_path
        self.vectorizers_path = vectorizers_path
        self.vectorizer = vectorizer

    def create_best_validation_results_table(self):
        text_column, column_names = self.data_manipulation.get_column_names()
        best_acc, best_f1, best_prec, best_rec = [], [], [], []
        validation_table = pd.DataFrame(columns = ['label', 'model', 'accuracy', 
                                                    'f1_score', 'precision',
                                                    'recall'])
        
        for i, label in enumerate(self.validation_results):
            acc, f1, prec, rec = [], [], [], []

            for j, model in enumerate(label):
                acc.append(round(model['mean_test_Accuracy'][0], 2))
                f1.append(round(model['mean_test_F1-Score'][0], 2))
                prec.append(round(model['mean_test_Precision'][0], 2))
                rec.append(round(model['mean_test_Recall'][0], 2))

            best_acc.append(acc[prec.index(max(prec))])
            best_f1.append(f1[prec.index(max(prec))])
            best_prec.append([prec.index(max(prec)), prec[prec.index(max(prec))]])
            best_rec.append(rec[prec.index(max(prec))])

            validation_table = validation_table.append({
                'label': column_names[i],
                'model': self.model_names[best_prec[i][0]], 
                'accuracy': best_acc[i], 
                'f1_score': best_f1[i], 
                'precision': best_prec[i][1],
                'recall': best_rec[i],
            }, ignore_index = True)

        return validation_table

    def import_models(self):
        text_column, column_names = self.data_manipulation.get_column_names()
        final_models, final_vectorizers = [], []

        for i, label in enumerate(column_names):
            try:
                file = joblib.load(f'{self.models_path}{label}_model.pkl')
                if file:
                    final_models.append(joblib.load(
                                                    f'{self.models_path}{label}_model.pkl'))
                    final_vectorizers.append(joblib.load(
                                        f'{self.vectorizers_path}{label}_vectorizer.pkl'))
            except FileNotFoundError:
                pass

        return final_models, final_vectorizers

    def test_results(self):
        text_column, column_names = self.data_manipulation.get_column_names()
        test_subsets = self.data_manipulation.create_test_subsets()
        final_models, final_vectorizers = self.import_models()

        for i, model in enumerate(final_models):
            # Creating an instace of FeatureExtraction class
            feats = FeatureExtraction(data = test_subsets[i], 
                                    text_column = text_column, 
                                    lemma = self.machine_learning.lemma, 
                                    pos = self.machine_learning.pos, 
                                    tag = self.machine_learning.tag,                                
                                    other_features = self.machine_learning.other_features,
                                    vectorizer = self.machine_learning.vectorizer,
                                    oth_feats_vectorizer = self.machine_learning.oth_feats_vectorizer)
            
            # Adding extra features to our test data
            test_data = feats.add_features_to_test()

            tf_idf = self.vectorizer(vocabulary = final_vectorizers[i], 
                                    lowercase = False)

            X_test = tf_idf.fit_transform(test_data[text_column].apply(lambda x: np.str_(x)))
            y_test = test_subsets[i][column_names[i]].astype('int')

            y_preds = final_models[i].predict(X_test)
            report = classification_report(y_test, y_preds)
            matrix = confusion_matrix(y_test, y_preds)

            print(f'Test {column_names[i]} subset for its best validation model \
                    {final_models[i]}')
            print('Classification report')
            print(report)

            print('Confusion matrix')
            print(matrix)
            print('')

    def test_results_over_all_models(self):
        text_column, column_names = self.data_manipulation.get_column_names()
        test_subsets = self.data_manipulation.create_test_subsets()
        _, data_test = self.data_manipulation.get_train_and_test_data() ##Aqui

        final_models, final_vectorizers = self.import_models()
        best_prec = []
        
        # Obtaining best models by its precision
        for i, label in enumerate(self.validation_results):
            prec = []

            for j, model in enumerate(label):
                prec.append(round(model['mean_test_Precision'][0], 2))
        
            best_prec.append(prec.index(max(prec)))

        # Obtaining best model names
        final_model_names = []
        for best_name in best_prec:
            for i, name in enumerate(self.model_names):
                if best_name == i:
                    final_model_names.append(name)
        
        # Creating an instace of FeatureExtraction class
        feats = FeatureExtraction(data = data_test, 
                                text_column = text_column, 
                                lemma = self.machine_learning.lemma, 
                                pos = self.machine_learning.pos, 
                                tag = self.machine_learning.tag,                                
                                other_features = self.machine_learning.other_features,
                                vectorizer = self.machine_learning.vectorizer,
                                oth_feats_vectorizer = self.machine_learning.oth_feats_vectorizer)
        
        # Adding extra features to our test data
        data_test = feats.add_features_to_test()

        # Obtaining prediction vectors
        final_classes = []
        for i, row in data_test.iterrows():
            classes = []

            for j, model in enumerate(final_models):
                tf_idf = self.vectorizer(vocabulary = final_vectorizers[j], lowercase = False)
                X_test = tf_idf.fit_transform([row[text_column]])

                classes.append(round(model.predict_proba(X_test).flatten().tolist()[1], 
                                    4))
        
            final_classes.append(classes)
        
        y_test = data_test[column_names].astype('int')

        # Selecting best prediction and converting into zeros and ones
        y_preds = []
        for pred in final_classes: 
            lista = [0] * len(final_model_names)
            idx = pred.index(max(pred))
            lista[idx] = 1
            y_preds.append(lista)

        # Converting y_test dataframe into list
        y_test = y_test.values.tolist()

        # Variables
        y_true = np.array(y_test)
        y_pred = np.array(y_preds)
        labels = column_names
        conf_mat_dict = {}
        validation_table = pd.DataFrame(columns = ['label', 'model','f1_score', 
                                                'precision', 'recall'])

        # Plotting confusion matrix
        y_true_, y_pred_ = [], []

        for y in y_true:
            for j, value in enumerate(y):
                if y[j] == 1:
                    y_true_.append(j)

        for y in y_pred:
            for j, value in enumerate(y):
                if y[j] == 1:
                    y_pred_.append(j)

        conf_matrix = confusion_matrix(y_true_, y_pred_)
        matrix_proportions = np.zeros((len(column_names), len(column_names)))

        for i in range(0, len(column_names)):
            matrix_proportions[i,:] = conf_matrix[i,:] / float(conf_matrix[i,:].sum())

        confusion_df = pd.DataFrame(matrix_proportions, index = column_names, 
                                    columns = column_names)
        plt.figure(figsize = (10, 10))
        sns.heatmap(confusion_df, annot = True, annot_kws = {'size': 12}, 
                    cmap = 'gist_gray_r', cbar = False, square = True, fmt = '.2f')
        plt.ylabel(r'Categorías verdaderas', fontsize = 14)
        plt.xlabel(r'Categorías predichas', fontsize = 14)
        plt.tick_params(labelsize = 12)                                                
        
        # Obtaining confusion matrix
        for label_col in range(len(final_model_names)):
            y_true_label = y_true[:, label_col]
            y_pred_label = y_pred[:, label_col]
            conf_mat_dict[labels[label_col]] = confusion_matrix(y_pred = y_pred_label, 
                                                                y_true = y_true_label)
        
        # Showing results
        bandera = 0
        for label, matrix in conf_mat_dict.items():
            TN, FP, FN, TP = matrix.ravel()

            if (TP + FP) == 0:
                precision = 0
            else:
                precision = round(TP / (TP + FP), 4)
            
            if (TP + FN) == 0:
                recall = 0
            else:
                recall = round(TP / (TP + FN), 4)

            if (precision + recall) == 0:
                f1_score = 0
            else:
                f1_score = round((2 * precision * recall) / (precision + recall), 4)

            validation_table = validation_table.append({
                    'label': label,
                    'model': final_model_names[bandera],
                    'f1_score': f1_score, 
                    'precision': precision,
                    'recall': recall,
                }, ignore_index = True)
            
            bandera += 1

        return validation_table