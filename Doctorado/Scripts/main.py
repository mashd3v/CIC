# Basic imports
import os, numpy as np, pandas as pd

# Vectorizers
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# ML Algorithms
from sklearn.linear_model import LogisticRegression, Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import CalibratedClassifierCV

# Scripts
import text_preprocessing as preprocessing
import feature_extraction as feature_extraction
import baseline_model as baseline
import plots as plt
import robust_classic_model as robust_model


# Main class
class Main:
    def __init__(
        self,
        data,
        text_column,
        label_column
        language,
        is_tweet,
        convert_tweet_tags,
        remove_stopwords,
        lemmatize,
        translate_emojis,
        whitelist,
        vectorizer,
        preprocess_data,
    ):
        self.data = data
        self.text_column = text_column
        self.label_column = label_column
        self.language = language
        self.is_tweet = is_tweet
        self.convert_tweet_tags = convert_tweet_tags
        self.remove_stopwords = remove_stopwords
        self.lemmatize = lemmatize
        self.translate_emojis = translate_emojis
        self.whitelist = whitelist
        self.vectorizer = vectorizer
        self.preprocess_data = preprocess_data

        if self.language == "english":
            self.lan = "en"
        elif self.language == "spanish":
            self.lan = "es"

        # Preprocess text data
        if self.preprocess_data:
            # Creating text preprocessing object
            prep = preprocessing.Preprocessing(language=self.language)

            # Loop for cleaning data
            data_preprocessed = []
            for d in self.data:
                data_prep = prep.main_preprocess(
                    data=d,
                    column="tweet",
                    tweet=True,
                    tweet_tags=True,
                    remove_stop_words=None,
                    lemmatize=False,
                    translate_emojis=False,
                    whitelist="",
                )
                data_preprocessed.append(data_prep)

        # Extracting features
        for i, d in enumerate(data_preprocessed):
            features = feature_extraction.FeatureExtraction(data=d,
                                                            text_column='tweet', 
                                                            lemma=True, 
                                                            pos=True, 
                                                            tag=True,                                
                                                            other_features=True,
                                                            vectorizer=self.vectorizer,
                                                            oth_feats_vectorizer=self.vectorizer,
                                                            language='es')
            
            # Getting training features
            if i == 0:
                training_dataframe = features.add_features()
            
            # Getting training features
            else:
                test_dataframe = features.add_features()
