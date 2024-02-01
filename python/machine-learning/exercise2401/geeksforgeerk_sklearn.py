#!/usr/bin/env python3

"""
Learning Model Building in Scikit-learn : A Python Machine Learning Library
https://www.geeksforgeeks.org/learning-model-building-scikit-learn-python-machine-learning-library/
"""

import os
import sys
import urllib.error
from urllib import request

# Step 1: Load a dataset

def loading_examplar_dataset() -> None:
    """ scikit-learn comes loaded with a few example datasets like the iris and digits datasets for classification and the boston house prices dataset for regression. """

    # load the iris dataset as an example
    from sklearn.datasets import load_iris
    iris = load_iris()

    # store the feature matrix (X) and response vector(v)
    X = iris.data
    y = iris.target

    # store the feature and target names
    feature_names = iris.feature_names
    target_names = iris.target_names

    # printing feature and target name of our dataset
    print("Feature names:", feature_names)
    print("Target names:", target_names)

    # X and y are numpy arrays
    print("\nType of X is:", type(X))
    
    # printing first 5 input rows
    print("\nFirst 5 rows of X:\n", X[:5])

def loading_external_dataset(file_path: str="weather.csv") -> None:
    """In pandas, important data types are:
    Series: Series is a one-dimensional labeled array capable of holding any data type.

    DataFrame: It is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object.
Note: The CSV file used in the example below can be downloaded from here:
    [weather.csv](http://www.sharecsv.com/dl/327fb8f66f90a98c2ed4454665efae9d/weather.csv)"""

    import pandas as pd

    # reading csv file
    data = pd.read_csv(file_path)
   
    # shape of dataset
    print("Shape:", data.shape)

    # column names
    print("\nFeatures:", data.columns)

    # storing the deature matrix (X) and response vector (y)
    X = data[data.columns[:-1]]
    y = data[data.columns[-1]]

    # printing first 5 rows of feature matrix
    print("\nFeature matrix:\n", X.head())

    # printing first 5 values of response vector
    print("\nResponse vector:\n", y.head())

# Step 2: Spliting the dataset

def advantages_of_train_test_split() -> None:
    """Split the dataset into two pieces: a training set and a testing set.
Train the model on the training set.
Test the model on the testing set, and evaluate how well our model did."""

    from sklearn.datasets import load_iris
    iris = load_iris()

    # stroe the feature matrix (X) and reponse vector (y)
    X = iris.data
    y = iris.target

    # splitting X and y into training and testing sets
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y,
        test_size=0.4, random_state=1)

    # printing the shapes of the new X objects
    print(X_train.shape, X_test.shape)

    # printing the shape of the new y objects
    print(y_train.shape, y_test.shape)    

# Step 3: Training the model

def knn_classifier(dir_path:str = None) -> None:
    """Scikit-learn provides a wide range of machine learning algorithms that have a unified/consistent interface for fitting, predicting accuracy, etc.
The example given below uses KNN (K nearest neighbors) classifier.

"""

    # load the iris dataset as an example
    from sklearn.datasets import load_iris
    iris = load_iris()

    # store the feature matrix (X) and response vector (y)
    X = iris.data
    y = iris.target

    # spliting X and y into training and testing sets
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

    # training the model on training set
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)

    # making predictions on the testing set
    y_pred = knn.predict(X_test)

    # comparing actual reponse values (y_test) with predicted reponse values
    from sklearn import metrics
    print("KNN model accuracy:", metrics.accuracy_score(y_test, y_pred))

    # making prediction for out of sample data
    sample = [[3, 5, 4, 2], [2, 3, 5, 4]]
    preds = knn.predict(sample)
    pred_species = [iris.target_names[p] for p in preds]
    print("Predictions:", pred_species)

    # saving the model
    try:
        from sklearn.externals import joblib
    except ImportError:
        # If you are using an older version of Scikit-learn (version 0.22 or earlier), you can upgrade to a newer version (version 0.23 or later) where ‘joblib’ has been moved to the ‘sklearn.utils’ package
        # https://itsourcecode.com/importerror/importerror-cannot-import-name-joblib-from-sklearn-externals/#:~:text=Solutions%20Importerror%3A%20cannot%20import%20name%20%E2%80%98joblib%E2%80%99%20from%20%E2%80%98sklearn.externals%E2%80%99,the%20import%20statement%20...%204%20Downgrade%20joblib%20
        import joblib
    file_path = 'iris_knn.pkl' if dir_path is None else \
        os.path.join(dir_path, 'iris_knn.pkl') 
    joblib.dump(knn, file_path)

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    n = len(sys.argv)
    for i in range(1, n):
        if sys.argv[i] == "load-examplar-dataset":
            sys.exit(loading_examplar_dataset())
        elif sys.argv[i] == "load-external-dataset":
            file_path = os.path.join(os.path.dirname(dir_path), "weather.csv")
            if os.path.exists(file_path) is False:
                try:
                    resp = request.urlopen("http://www.sharecsv.com/dl/327fb8f66f90a98c2ed4454665efae9d/weather.csv")
                    f = open(file_path, 'w')
                    f.write(resp.read())
                except urllib.error.URLError as err:
                    raise RuntimeError("URL error") from err
                except OSError as err:
                    raise RuntimeError("IO error") from err
                
            sys.exit(loading_external_dataset(file_path))
        elif sys.argv[i] == "split-train-test":
            sys.exit(advantages_of_train_test_split())
        elif sys.argv[i] == "train-knn-model":
            sys.exit(knn_classifier(os.path.dirname(dir_path)))

    print('''Usage: <scriptPath> <arguments>
Arguments: 
    load-examplar-dataset
    load-external-dataset
    split-train-test
    train-knn-model''')


