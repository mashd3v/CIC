import sys
sys.path.append("../Scripts")

# Imports
import os
import pandas as pd
import numpy as np

# Scripts import
import text_preprocessing as preprocessing
import feature_extraction as feature_extraction
import baseline_model as baseline
import plots as plt
import robust_classic_model as robust_model

# Sklearn models
from sklearn.linear_model import LogisticRegression, Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import CalibratedClassifierCV

# Sklearn NLP imports
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

def read_data(path, file_names):
    """
    Read data from a file, if the file is a csv file, it will be read as a pandas DataFrame. 
    If it is a txt file, it will be read as a numpy array. If it is a json file, it will be 
    read as a dictionary

    Argument 'path' is a String. The path is the path to the folder where the file is located.
    Argument 'file_names' is a list of strings. The list contains the names of the files to be 
    read.

    :param path: path to the folder where the file is located
    :param file_names: list of strings. The list contains the names of the files to be read.
    :return: list of data. Each element of the list is a data read from a file.
    """
    # List to store the data
    data_list = []

    # Reading the data
    for i, file_name in enumerate(file_names):
        if '.csv' in file_name:
            data = pd.read_csv(os.path.join(path, file_name))
        elif '.txt' in file_name:
            continue
        elif '.json' in file_name:
            continue
        data_list.append(data)
    
    return data_list

def preprocess_text(data, text_column, language, is_tweet, remove_stopwords, lemmatize, 
                    translate_emojis, whitelist_words=None):
    """
    Preprocess text data. This function calls the preprocessing function from the preprocessing
    script.

    Argument 'data' is a list of a pandas DataFrame. The DataFrame list contains the data to be 
    preprocessed. The order of the dataframes in the list must be training data and then test data.
    Argument 'text_column' is a String. The String is the name of the column that contains the
    text data.
    Argument 'language' is a String. The String is the language of the text data.
    Argument 'is_tweet' is a boolean. If True, the text data will be preprocessed for tweets.
    Argument 'remove_stopwords' is a boolean. If True, the stopwords will be removed from the
    text data.
    Argument 'lemmatize' is a boolean. If True, the text data will be lemmatized.
    Argument 'translate_emojis' is a boolean. If True, the emojis will be translated to text.
    Argument 'whitelist_words' is a list of strings. The list contains the words that will be
    whitelisted.

    :param data: list of a pandas DataFrame. The DataFrame list contains the data to be
    preprocessed.
    :param text_column: String. The String is the name of the column that contains the text data.
    :param language: String. The String is the language of the text data.
    :param is_tweet: boolean. If True, the text data will be preprocessed for tweets.
    :param remove_stopwords: boolean. If True, the stopwords will be removed from the text data.
    :param lemmatize: boolean. If True, the text data will be lemmatized.
    :param translate_emojis: boolean. If True, the emojis will be translated to text.
    :param whitelist_words: list of strings. The list contains the words that will be whitelisted.
    :return: list of a pandas DataFrame. The DataFrame list contains the preprocessed data.
    """
    # New list to store the preprocessed data
    data_preprocessed = []
    
    # If is_tweet is True, the tweets will be preprocessed
    if is_tweet:
        tweet_tags = True
    else:
        tweet_tags = False

    # If whitelist_words is not None, the whitelist will be the list of words
    if whitelist_words != None:
        whitelist = whitelist
    else:
        whitelist = ""

    # Initializing the preprocessing class
    prep = preprocessing.Preprocessing(language=language)
    
    # Preprocessing the data
    for new_data in data:
        preprocessed_data = prep.main_preprocess(data=new_data,
                                                column=text_column,
                                                tweet=is_tweet,
                                                tweet_tags=tweet_tags,
                                                remove_stop_words=remove_stopwords,
                                                lemmatize=lemmatize,
                                                translate_emojis=translate_emojis,
                                                whitelist=whitelist)
        data_preprocessed.append(preprocessed_data)
    
    return data_preprocessed

def extract_features(data, text_column, language, lemma, pos_tag, tag, other_features, vectorizer):
    """
    Extract features from text data. This function calls the feature extraction function from the
    feature extraction script.

    Argument 'data' is a list of a pandas DataFrame. The DataFrame list contains the data to be
    preprocessed. The order of the DataFrames in the list must be training data and then test data.
    Argument 'text_column' is a String. The String is the name of the column that contains the
    text data.
    Argument 'language' is a String. The String is the language of the text data.
    Argument 'lemma' is a boolean. If True, the text data will be lemmatized.
    Argument 'pos_tag' is a boolean. If True, the text data will be POS tagged.
    Argument 'tag' is a boolean. If True, the text data will be tagged.
    Argument 'other_features' is a boolean. If True, the other features will be extracted.
    Argument 'Vectorizer' is a scikit-learn Vectorizer. The Vectorizer is the way of extracting
    the features.

    :param data: list of a pandas DataFrame. The DataFrame list contains the data to be
    preprocessed.
    :param text_column: String. The String is the name of the column that contains the text data.
    :param language: String. The String is the language of the text data.
    :param lemma: boolean. If True, the text data will be lemmatized.
    :param pos_tag: boolean. If True, the text data will be POS tagged.
    :param tag: boolean. If True, the text data will be tagged.
    :param other_features: boolean. If True, the other features will be extracted.
    :param Vectorizer: scikit-learn Vectorizer. The Vectorizer is the way of extracting the
    features.
    :return: list of a pandas DataFrame. The DataFrame list contains the preprocessed data.
    """

    # Language dict
    language_dict = {'spanish': 'es', 'english': 'en'}

    # New list to store the preprocessed data
    data_preprocessed = []

    # Creating another vectorizer for the other features
    other_features_vectorizer = vectorizer

    # Getting the features
    for i, data_features in enumerate(data):
        features = feature_extraction.FeatureExtraction(data=data_features,
                                        text_column=text_column,
                                        lemma=lemma,
                                        pos=pos_tag,
                                        tag=tag,
                                        other_features=other_features,
                                        vectorizer=vectorizer,
                                        oth_feats_vectorizer=other_features_vectorizer,
                                        language=language_dict[language])

        new_data = features.add_features()
        data_preprocessed.append(new_data)
    
    return data_preprocessed

def ml_baselines(data, text_column, target_column, target_names, plot_results, ngram_range=(1,1), 
                 min_df=3):
    """
    Machine learning baseline models. This function calls the machine learning baseline models
    from the machine learning baseline script.

    Argument 'data' is a list of a pandas DataFrame. The DataFrame list contains the data to be
    preprocessed. The order of the DataFrames in the list must be training data and then test data.
    Argument 'text_column' is a String. The String is the name of the column that contains the
    text data.
    Argument 'target_column' is a String. The String is the name of the column that contains the
    target data.
    Argument 'target_names' is a String list. The list contains the name of the diferent targets
    the data has.
    Argument 'plot_results' is a boolean. If True, the results will be plotted.
    Argument 'ngram_range' is a tuple. The tuple contains the range of ngrams to be used.
    Argument 'min_df' is an integer. The integer is the minimum frequency of a word to be used.

    :param data: list of a pandas DataFrame. The DataFrame list contains the data to be
    preprocessed.
    :param text_column: String. The String is the name of the column that contains the text data.
    :param target_column: String. The String is the name of the column that contains the target
    data.
    :param target_names: String list. The list contains the name of the diferent targets the data
    has.
    :param plot_results: boolean. If True, the results will be plotted.
    :param ngram_range: tuple. The tuple contains the range of ngrams to be used.
    :param min_df: integer. The integer is the minimum frequency of a word to be used.
    :return: list of a pandas DataFrame. The DataFrame list contains the preprocessed data.
    """

    # Models
    models = [LogisticRegression(), 
            RandomForestClassifier(), 
            CalibratedClassifierCV(LinearSVC()), 
            MultinomialNB(), 
            MLPClassifier(), 
            CalibratedClassifierCV(Perceptron()), 
            KNeighborsClassifier()]
    
    model_names = ['Logistic Regression',
                'Random Forest',
                'Linear SVC',
                'Multinomial Naive Bayes',
                'MLP Classifier',
                'Perceptron',
                'K Neighbors Classifier']
    
    # New lists to store the final results
    final_models, final_vectorizers, final_metrics = [], [], []

    # Getting the results
    for i, model in enumerate(models):
        base = baseline.Baseline(model=model,
                                train_data=data[0],
                                test_data=data[1],
                                x_label_column=text_column,
                                y_label_column=target_column,
                                ngram_range=ngram_range,
                                min_df=min_df,
                                model_name=model_names[i],
                                target_names=target_names)
        
        final_model, vectorizer, metrics = base.baseline()

        # Printing classification report
        print(metrics[0])
        
        # Appending the final results
        final_models.append(final_model)
        final_vectorizers.append(vectorizer)
        final_metrics.append(metrics)

        # Plotting the results
        if plot_results:
            plots = plt.Plots(metrics=metrics)
            plots.plot_classification_report(title=f'Classification Report\nModel: {model_names[i]}-baseline',
                                            x_label='Metrics',
                                            y_label='Score',
                                            x_labels=['Precision', 'Recall', 'F1-Score'],
                                            y_labels=target_names)
            plots.plot_confusion_matrix(title=f'Confusion Matrix\nModel: {model_names[i]}-baseline',
                                        x_label='Predicted',
                                        y_label='True',
                                        labels=target_names)
    
    return final_models, final_vectorizers, final_metrics
