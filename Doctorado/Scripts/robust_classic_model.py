# Required installations
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np
import joblib
from sklearn import metrics
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from feature_extraction import FeatureExtraction
from sklearn.decomposition import PCA
import subprocess

subprocess.run(["python3", "-m", "pip", "install", "joblib==1.1.0"])

# Imports
# Feature extraction

# Tools to split data and evaluate model performance

# Metrics

# Library to save models

# This library offers comprehensive mathematical functions

# NLP Vectorizers

# NLP library


class RobustMachineLearningModel:
    def __init__(
        self,
        models,
        model_names,
        train_data,
        x_label_column,
        y_label_column,
        folds,
        grid_params,
        path_to_save_models,
        path_to_save_vectorizer,
        lemma,
        pos,
        tag,
        other_features,
        vectorizer,
        oth_feats_vectorizer,
        language,
    ):
        self.models = models
        self.model_names = model_names
        self.train_data = train_data
        self.x_label_column = x_label_column
        self.y_label_column = y_label_column
        self.folds = folds
        self.grid_params = grid_params
        self.path_to_save_models = path_to_save_models
        self.path_to_save_vectorizer = path_to_save_vectorizer
        self.lemma = lemma
        self.pos = pos
        self.tag = tag
        self.other_features = other_features
        self.vectorizer = vectorizer
        self.oth_feats_vectorizer = oth_feats_vectorizer
        self.language = language

    def get_best_cross_validation(self):
        scoring = {
            "Accuracy": "accuracy",
            "F1-Score": "f1",
            "Precision": "precision",
            "Recall": "recall",
        }

        # List to store the best models
        # 'best_models_per_label' should be a list of models with the same number of
        # existing labels.

        feats_train = FeatureExtraction(
            data=self.train_data,
            text_column=self.x_label_column,
            lemma=self.lemma,
            pos=self.pos,
            tag=self.tag,
            other_features=self.other_features,
            vectorizer=self.vectorizer,
            oth_feats_vectorizer=self.oth_feats_vectorizer,
            language=self.language,
        )

        (
            final_vector_train,
            final_volcabulary_train,
            final_dataframes_train,
        ) = feats_train.features()

        # X and Y train
        X_train = final_vector_train
        y_train = self.train_data[self.y_label_column].tolist()

        # Finding the best model
        for j, model in enumerate(self.models):
            print(f"Model {j}: {self.model_names[j]}")
            kFold_cv = KFold(n_splits=self.folds, shuffle=True, random_state=42)
            param_grid = self.grid_params
            grid_search = GridSearchCV(
                model,
                param_grid[j],
                cv=kFold_cv.split(X_train, y_train),
                scoring="f1_macro",
                verbose=3,
                return_train_score=True,
            )
            grid_search.fit(X_train, y_train)

            print("tuned hpyerparameters :(best parameters) ", grid_search.best_params_)
            print("accuracy :", grid_search.best_score_)

    def get_best_cross_validation_pca(self):
        scoring = {
            "Accuracy": "accuracy",
            "F1-Score": "f1",
            "Precision": "precision",
            "Recall": "recall",
        }

        # List to store the best models
        # 'best_models_per_label' should be a list of models with the same number of
        # existing labels.

        feats_train = FeatureExtraction(
            data=self.train_data,
            text_column=self.x_label_column,
            lemma=self.lemma,
            pos=self.pos,
            tag=self.tag,
            other_features=self.other_features,
            vectorizer=self.vectorizer,
            oth_feats_vectorizer=self.oth_feats_vectorizer,
            language=self.language,
        )

        data = feats_train.add_features_to_test()

        # X and Y train
        X_train = data[self.x_label_column]
        X_vec = self.vectorizer.fit_transform(X_train)
        pca = PCA(n_components=1000)
        X_pca = pca.fit_transform(X_vec.toarray())
        y_train = self.train_data[self.y_label_column].tolist()

        # Finding the best model
        for j, model in enumerate(self.models):
            print(f"Model {j}: {self.model_names[j]}")
            kFold_cv = KFold(n_splits=self.folds, shuffle=True, random_state=42)
            param_grid = self.grid_params
            grid_search = GridSearchCV(
                model,
                param_grid[j],
                cv=kFold_cv.split(X_pca, y_train),
                scoring="f1_macro",
                verbose=3,
                return_train_score=True,
            )
            grid_search.fit(X_pca, y_train)

            print("Best parameters: ", grid_search.best_params_)
            print("Accuracy :", grid_search.best_score_)
