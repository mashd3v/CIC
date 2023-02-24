'''Imports'''
import pandas as pd
from sklearn.model_selection import train_test_split

'''Data manipulation class'''
class DataManipulation:
    def __init__(self, dataset_path, seed, test_size, any_label_is_clean_data,
                clean_data_label):
        self.dataset_path = dataset_path
        self.seed = seed
        self.test_size = test_size
        self.any_label_is_clean_data = any_label_is_clean_data
        self.clean_data_label = clean_data_label

    # Function to return the dataset
    def read_dataset(self):
        return pd.read_csv(self.dataset_path)
    
    # Funtion to obtain seed
    def get_seed(self):
        return self.seed

    # Function to obtain the column names
    def get_column_names(self):
        dataset = self.read_dataset()
        column_names = []

        for column in dataset.columns:
            column_names.append(column)
        
        text_column = column_names[0]
        column_names.pop(0)
        
        return text_column, column_names

    # Function to obtain train and test data
    def get_train_and_test_data(self):
        dataset = self.read_dataset()
        dataset = dataset.dropna()
        data_train, data_test = train_test_split(dataset, random_state = self.seed, 
                                            test_size = self.test_size)
        return data_train, data_test

    # Function to create labeled subsets, this function includes the clean subset
    def create_labeled_subsets(self):
        data_train, data_test = self.get_train_and_test_data()
        text_column, column_names = self.get_column_names()
        labeled_subsets = []
        
        # Drop NA items from training data
        data_train = data_train.dropna()

        for label in column_names:
            labels = column_names.copy()
            labels.remove(label)

            # Creating query in order to obtain only labeled data
            query = ''
            for i, query_label in enumerate(column_names):
                if label == query_label:
                    if i == len(column_names) - 1:
                        query += query_label + ' == 1'
                    else:
                        query += query_label + ' == 1 and '
                else: 
                    if i == len(column_names) - 1:
                        query += query_label + ' == 0'
                    else:
                        query += query_label + ' == 0 and '

            labeled_subset = data_train.query(query)
            labeled_subsets.append(labeled_subset.drop(labels, axis = 1))

        if self.any_label_is_clean_data:
            for i, label in enumerate(column_names):
                if label == self.clean_data_label:
                    clean_subset = labeled_subsets[i].copy()
                    break
            clean_subset.rename(columns = {self.clean_data_label: 'clean_data'},
                                inplace = True)
            clean_subset.loc[clean_subset['clean_data'] == 1, 'clean_data'] = 0
        else:  
            clean_query = ''
            for i, label in enumerate(column_names):
                if i == len(column_names) - 1:
                    clean_query += label + ' == 0'
                else:
                    clean_query += label + ' == 0 and '
            
            clean_subset = data_train.query(clean_query)
            clean_subset = clean_subset.drop(clean_subset.columns[2:], axis = 1)
            clean_subset.rename(columns = {column_names[0]: 'clean_data'},
                                inplace = True)

        return labeled_subsets, clean_subset

    # Function to create test subsets
    def create_test_subsets(self):
        data_train, data_test = self.get_train_and_test_data()
        text_column, column_names = self.get_column_names()
        test_subsets = []
        
        for label in column_names:
            test_subset = data_test.loc[:, [text_column, label]]
            test_subsets.append(test_subset)

        return test_subsets

    # Function to balance subsets
    def balance_subsets(self):
        labeled_subsets, clean_subset = self.create_labeled_subsets()
        text_column, column_names = self.get_column_names()
        balanced_subsets = []

        for i, subset in enumerate(labeled_subsets):
            if subset.shape[0] != 0:
                if column_names[i] == self.clean_data_label:
                    new_subsets = labeled_subsets.copy()
                    new_subsets.pop(i)

                    new_labeled = []
                    for j, labeled_subset in enumerate(new_subsets):
                        labeled_subset.replace(1, 0, inplace = True)
                        labeled_subset.rename(columns = {column_names[j]: column_names[i]},
                                        inplace = True)
                        new_labeled.append(labeled_subset)

                    labeled_df = pd.concat(new_labeled, ignore_index = True)
                    subset = pd.concat([subset, labeled_df.sample(
                                                            n = labeled_subsets[i].shape[0], 
                                                            random_state = self.seed)])
                    balanced_subsets.append(subset)
                else:
                    clean = clean_subset.copy()
                    clean.rename(columns = {'clean_data': column_names[i]},
                                        inplace = True)
                    if subset.shape[0] < clean.shape[0]:
                        subset = pd.concat([subset, clean[:subset.shape[0]]], 
                                        ignore_index = True)
                    else:
                        subset = pd.concat([subset[:clean.shape[0]], clean], 
                                        ignore_index = True)
                    balanced_subsets.append(subset)
            else:
                balanced_subsets.append(subset)
        return balanced_subsets

    # Function to check the distribution of each label to check if data balancing
    # worked
    def subsets_summary_table(self):
        # Creating dataframe to display the previous balanced subsets
        text_column, column_names = self.get_column_names()
        subsets = self.balance_subsets()

        table_data = pd.DataFrame()
        df = pd.DataFrame(columns = column_names)

        '''
        NOTE: the array of column_names and subsets must correspond to each other 
        with their indices. That is:
        column_names = [toxic, very_toxic]
        subsets = [toxic_data, very_toxic_data]
        '''
        # Filling dataframe
        for i, d in enumerate(subsets):
            if d.shape[0] == 0:
                dataset = [0, 0]
            else:
                dataset = d[column_names[i]].value_counts().to_frame().values.flatten()
            table_data = table_data.append({'name': column_names[i],
                                            'toxic_comments': dataset[0], 
                                            'clean_comments': dataset[1], 
                                            'total_data': dataset[0] + dataset[1]}, 
                                            ignore_index = True)
        return table_data
