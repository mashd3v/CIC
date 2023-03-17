# Imports
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# Main class
class Baseline:
    def __init__(self, model, train_data, test_data, x_label_column, y_label_column, target_names):
        self.model = model
        self.train_data = train_data
        self.test_data = test_data
        self.x_label_column = x_label_column
        self.y_label_column = y_label_column
        self.target_names = target_names

    
    def baseline(self):
        # Training data
        x_train = self.train_data[self.x_label_column].tolist()
        y_train = self.train_data[self.y_label_column].tolist()

        # Test data
        x_test = self.test_data[self.x_label_column].tolist()
        y_test = self.test_data[self.y_label_column].tolist()

        # Vectorizing text data
        vectorizer = TfidfVectorizer(ngram_range=(1, 3), min_df=3)
        x_train = vectorizer.fit_transform(x_train)
        x_test = vectorizer.transform(x_test)

        # Fitting model
        print(f'Fitting {self.y_label_column} model')
        final_model = self.model
        final_model.fit(x_train, y_train)
        y_pred = final_model.predict(x_test)

        # Results
        print(metrics.classification_report(y_test, 
                                            y_pred, 
                                            target_names=self.target_names))


        return final_model, vectorizer
