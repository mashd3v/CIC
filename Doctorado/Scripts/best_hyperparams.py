import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from sklearn.model_selection import cross_val_score

class BestHyperparams:
    def __init__(self, ngram_ranges, min_dfs, data_train, data_test, text_column, class_column):
        self.ngram_ranges = ngram_ranges
        self.min_dfs = min_dfs
        self.data_train = data_train
        self.data_test = data_test
        self.text_column = text_column
        self.class_column = class_column


    def evaluate_model(self, params):
        clf_type = params['type']
        del params['type']
        
        if clf_type == 'lr':
            clf = LogisticRegression(**params)
        elif clf_type == 'svm':
            clf = LinearSVC(**params)
        elif clf_type == 'nb':
            clf = MultinomialNB(**params)
        elif clf_type == 'rf':
            clf = RandomForestClassifier(**params)
        
        scores = cross_val_score(clf, X_train_tfidf, y_train, cv=10, scoring='accuracy')
        return {'loss': -scores.mean(), 'status': STATUS_OK}


    def search_hyperparams(self):
        for ngram_range in self.ngram_ranges:
            for min_df in self.min_dfs:
                vectorizer = TfidfVectorizer(min_df=min_df, ngram_range=ngram_range)
                X_train_tfidf = vectorizer.fit_transform(self.data_train[self.text_column])
                X_test_tfidf = vectorizer.fit_transform(self.data_test[self.text_column])

                clf_space = {'type': hp.choice('type', 
                                               [{'type': 'lr', 'C': hp.loguniform('C_lr', -5, 2)},
                                                {'type': 'svm', 'C': hp.loguniform('C_svm', -5, 2)},
                                                {'type': 'nb', 'alpha': hp.uniform('alpha_nb', 0, 1)},
                                                {'type': 'rf', 'n_estimators': hp.choice('n_estimators_rf', range(50, 200, 10))}]
                                                )
                            }
                
                trials = Trials()
                best = fmin(fn=self.evaluate_model,
                            space=clf_space,
                            algo=tpe.suggest,
                            max_evals=100,
                            trials=trials)
                
                best_params = None
                for trial in trials.trials:
                    if best_params is None or trial['result']['loss'] < best_params['loss']:
                        best_params = trial['misc']['vals']
                best_params = {k:v[0] for k, v in best_params.items()}

                clf_type = best_params['type']
                del best_params['type']

                if clf_type == 0:
                    clf_type = 'lr'
                elif clf_type == 1:
                    clf_type = 'svm'
                elif clf_type == 2:
                    clf_type = 'nb'
                elif clf_type == 3:
                    clf_type = 'rf'
                
                if clf_type == 'lr':
                    clf = LogisticRegression(**best_params)
                elif clf_type == 'svm':
                    clf = LinearSVC(**best_params)
                elif clf_type == 'nb':
                    clf = MultinomialNB(**best_params)
                elif clf_type == 'rf':
                    clf = RandomForestClassifier(**best_params)

                clf.fit(X_train_tfidf, self.data_train[self.class_column])
                acc = clf.score(X_test_tfidf, self.data_test[self.class_column])
            print(f'Ngram Range: {ngram_range} - Min DF: {min_df} - Best Model: {clf_type} - Accuracy: {acc}')

