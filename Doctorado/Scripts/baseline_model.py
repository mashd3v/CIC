# Imports
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# Main class
class Baseline:
    def __init__(self, train_data, test_data, x_label_column, y_label_column, target_names):
        self.train_data = train_data
        self.test_data = test_data
        self.x_label_column = x_label_column
        self.y_label_column = y_label_column
        self.target_names = target_names

    
    def baseline(self, model, train_data, test_data, x_label_column, y_label_column, target_names):
        # Training data
        x_train = train_data[x_label_column].tolist()
        y_train = train_data[y_label_column].tolist()

        # Test data
        x_test = test_data[x_label_column].tolist()
        y_test = test_data[y_label_column].tolist()

        # Vectorizing text data
        vectorizer = TfidfVectorizer(ngram_range=(1, 3), min_df=3)
        x_train = vectorizer.fit_transform(x_train)
        x_test = vectorizer.transform(x_test)

        # Fitting model
        print(f'Fitting {y_label_column} model')
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)

        # Results
        print(metrics.classification_report(y_test, y_pred, target_names=target_names))


        return model, vectorizer
