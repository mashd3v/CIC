# Imports
import sys
sys.path.append('../Scripts')

# For cleaning data
import text_preprocessing_v2 as tp2
import pandas as pd, numpy as np

class CleaningTwitterData:
    def __init__(self, csv_path, sv_path, text_column, language, remove_stopwords, 
                 is_dataframe, emoji_path, dataframes, columns, dictionary_list):
        self.csv_path = csv_path
        self.sv_path = sv_path
        self.text_column = text_column
        self.language = language
        self.remove_stopwords = remove_stopwords
        self.is_dataframe = is_dataframe
        self.emoji_path = emoji_path
        self.dataframes = dataframes
        self.columns = columns
        self.dictionary_list = dictionary_list


    def clean_twitter_data(self, csv_path, text_column, language, remove_stopwords=False, 
                                is_dataframe=True, emoji_path=None):
        # Reading data
        data = pd.read_csv(csv_path)

        # Initializing tp2 object
        preprocessing = tp2.Preprocessing(language=language)

        # Run preprocessing main function
        data = preprocessing.main_preprocess(data=data,
                                            column=text_column,
                                            remove_stop_words=remove_stopwords,
                                            is_dataframe=is_dataframe,
                                            emoji_path=emoji_path)
        
        # Deleting NA values
        data = data.dropna(how='all')

        return data


    def change_to_numeric_labels(self, dataframes, columns, dictionary_list):
        for df in dataframes:
            for i, column in enumerate(columns):
                df[column].replace(list(dictionary_list[i].keys()), 
                                            list(dictionary_list[i].values()), 
                                            inplace=True)