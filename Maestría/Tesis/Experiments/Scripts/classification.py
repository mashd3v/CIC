'''Imports'''
# DataManipulation class
from data_manipulation import DataManipulation
# import data_manipulation as DataManipulation

# FeatureExtraction class
from feature_extraction import FeatureExtraction
# import feature_extraction as FeatureExtraction

# Tools to split data and evaluate model performance
from sklearn.model_selection import train_test_split, KFold, GridSearchCV

# One vs rest classifier
from sklearn.multiclass import OneVsRestClassifier

# Metrics
from sklearn.metrics import classification_report, multilabel_confusion_matrix

# Library to save models
import joblib

# This library offers comprehensive mathematical functions
import numpy as np

# NLP Vectorizers
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# Library to create dataclasses
from dataclasses import dataclass

# NLP library
import spacy
nlp = spacy.load("en_core_web_sm")

'''
  Notes: 
    * Make sure that paths to save models and vectorizers exists.
    * This class is only for training data
'''
@dataclass
class MachineLearning:
    def __init__(self, data_manipulation, models, model_names, folds, 
                path_to_save_models, path_to_save_vectorizer, lemma, pos, tag, 
                other_features, vectorizer, oth_feats_vectorizer):
        self.data_manipulation = data_manipulation
        self.models = models
        self.model_names = model_names
        self.folds = folds
        self.path_to_save_models = path_to_save_models
        self.path_to_save_vectorizer = path_to_save_vectorizer
        self.lemma = lemma
        self.pos = pos
        self.tag = tag
        self.other_features = other_features
        self.vectorizer = vectorizer
        self.oth_feats_vectorizer = oth_feats_vectorizer

    def get_best_cross_validation(self):
        text_column, column_names = self.data_manipulation.get_column_names()
        train_subsets = self.data_manipulation.balance_subsets()
        test_subsets = self.data_manipulation.create_test_subsets()
        scoring = {'Accuracy': 'accuracy', 'F1-Score': 'f1', 
                'Precision': 'precision', 'Recall': 'recall'}

        # Lists to save final results
        # 'best_models_per_label' should be a list of models with the same number of
        # existing labels.
        trained_models = []
        trained_vectorizers = []
        metrics = []
        precision_results = []
        vectorizers = []
        best_models_per_label = []

        for i, subset in enumerate(train_subsets):
            if subset.shape[0] != 0:
                globals()[f'models_{subset}'] = []
                globals()[f'{subset}_vectorizers'] = []
                globals()[f'metrics_{subset}'] = []
                globals()[f'precision_{subset}'] = []
            
                feats = FeatureExtraction(data = subset, 
                                    text_column = text_column, 
                                    lemma = self.lemma, 
                                    pos = self.pos, 
                                    tag = self.tag,                                
                                    other_features = self.other_features,
                                    vectorizer = self.vectorizer,
                                    oth_feats_vectorizer = self.oth_feats_vectorizer)
                
                final_vector, final_volcabulary, final_dataframes = feats.features()

                # X and Y train
                X_train = final_vector
                y_train = subset[column_names[i]].astype('int')
                
                print('')
                print(f'Subset {i}: {column_names[i]}')

                for j, model in enumerate(self.models):
                    print(f'Model {j}: {self.model_names[j]}')
                    
                    kFold_cv = KFold(n_splits = self.folds, 
                                    random_state = self.data_manipulation.seed, 
                                    shuffle = True)
                    param_grid = [{}] # Optionally you can add parameters
                    grid_search = GridSearchCV(model, 
                                                param_grid = param_grid,
                                                scoring = scoring,
                                                refit = 'Precision',
                                                cv = kFold_cv.split(X_train, y_train),
                                                verbose = 2, 
                                                return_train_score = True)
                    
                    # Training and saving model into models_subset list
                    final_model = grid_search.fit(X_train, y_train)
                    globals()[f'models_{subset}'].append(final_model)

                    # Training and saving vectorizer into subset_vectorizer list
                    globals()[f'{subset}_vectorizers'].append(final_volcabulary)

                    # Getting metrics and saving them into metrics_subset list
                    metric_results = final_model.cv_results_
                    globals()[f'metrics_{subset}'].append(metric_results)
                    
                    # Getting mean_train_score and saving it into precision_subset list
                    precision_result = round(final_model
                                            .cv_results_['mean_test_Precision'][0], 4)
                    globals()[f'precision_{subset}'].append(precision_result)

                # Saving data into final results variables
                trained_models.append(globals()[f'models_{subset}'])
                trained_vectorizers.append(globals()[f'{subset}_vectorizers'])
                metrics.append(globals()[f'metrics_{subset}'])
                precision_results.append(globals()[f'precision_{subset}'])

            else:
                print(f'Subset {column_names[i]} has no data')

        # Search the best models and saving them
        for i, model in enumerate(trained_models):
            pr = precision_results[i]
            best_models_per_label.append(model[pr.index(max(pr))])
            vectorizers.append(trained_vectorizers[i][pr.index(max(pr))])

        # Saving models and vectorizers
        for i, best_model_label in enumerate(best_models_per_label):
            joblib.dump(best_model_label.best_estimator_, 
                        f'{self.path_to_save_models}{column_names[i]}_model.pkl')
            joblib.dump(vectorizers[i], 
                    f'{self.path_to_save_vectorizer}{column_names[i]}_vectorizer.pkl')
        
        return train_subsets, trained_models, metrics, precision_results

    def one_vs_rest_classifier(self):
        data = self.data_manipulation.read_dataset()
        text_column, column_names = self.data_manipulation.get_column_names()

        for i, model in enumerate(self.models):
            print(f'One vs Rest - {self.model_names[i]} model')
            X_features = self.vectorizer.fit_transform(data[text_column].\
                                                        apply(lambda x: np.str_(x)))
            y = data[column_names].astype('int')
            X_train, X_test, y_train, y_test = train_test_split(X_features, 
                                        y, 
                                        test_size = self.data_manipulation.test_size,
                                        random_state = self.data_manipulation.seed)
            model_train = OneVsRestClassifier(model).fit(X_train, y_train)
            y_pred_test = model_train.predict(X_test)

            print('Classification report')
            print(classification_report(y_test, y_pred_test))

            print('Confusion matrix')
            print(multilabel_confusion_matrix(y_test, y_pred_test))
            print('')
