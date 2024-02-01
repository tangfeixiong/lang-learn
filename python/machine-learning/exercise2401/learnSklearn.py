#! /usr/bin/env python3

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import cross_val_score

def userGuide_TrainTestSplit():
    """
    https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation
    """
    X, y = datasets.load_iris(return_X_y=True)
    print(f'{X!r}', f'{y!r}', sep='\n')
    print(X.shape, y.shape)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
    print(X_train.shape, y_train.shape)
    print(X_test.shape, y_test.shape)
    clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
    print(clf.score(X_test, y_test))
    
    clf = svm.SVC(kernel='linear', C=1, random_state=42)
    scores = cross_val_score(clf, X, y, cv=5)
    print(scores)
    print(scores.mean(), scores.std())
    
    
def apiTrainTestSplit():
    X = [['a', 'b'],['c', 'd'],['e', 'f'],['g', 'h'],['i','j']]
    y = range(5)
    print(X, list(y), sep='\n')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    print(X_train, y_train, X_test, y_test, sep='\n')

    
def docExample_SimpleImputer():
    """
    https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html
    """

    import numpy as np
    from sklearn.impute import SimpleImputer
    imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
    imp_mean.fit([[7, 2, 3], [4, np.nan, 6], [10, 5, 0]])
    
    X = [[np.nan, 2, 3], [4, np.nan, 6], [10, np.nan, 9]]
    print(imp_mean.transform(X))

def userGuide_SimpleImputer():
    """
    https://scikit-learn.org/stable/modules/impute.html#impute
    """

    import numpy as np
    from sklearn.impute import SimpleImputer
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    imp.fit([[1, 2], [np.nan, 3], [7, 6]])
    X = [[np.nan, 2], [6, np.nan], [7, 6]]
    print(imp.transform(X))

    # supports scipy sparse matrices:
    import scipy.sparse as sp
    X = sp.csc_matrix([[1, 2], [0, -1], [8, 4]])
    imp = SimpleImputer(missing_values=-1, strategy='mean')
    imp.fit(X)
    X_test = sp.csc_matrix([[-1, 2], [6, -1], [7, 6]])
    print(imp.transform(X_test).toarray())

    # pandas categoricals
    import pandas as pd
    df = pd.DataFrame([["a", "x"],
                       [np.nan, "y"],
                       ["a", np.nan],
                       ["b", "y"]], dtype="category")
    imp = SimpleImputer(strategy="most_frequent")
    print(imp.fit_transform(df))


def docExample_OneHotEncoder():
    """
    https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html
    """

    from sklearn.preprocessing import OneHotEncoder
    enc = OneHotEncoder(handle_unknown='ignore')
    X = [['Male', 1], ['Female', 3], ['Female', 2]]
    enc.fit(X)
    print(enc.categories_)
    a = enc.transform([['Female', 1], ['Male', 4]]).toarray()
    print(repr(a))
    a = enc.inverse_transform([[0, 1, 1, 0, 0], [0, 0, 0, 1, 0]])
    print(repr(a))
    a = enc.get_feature_names_out(['gender', 'group'])
    print(repr(a))

    # drop the first column for each feature:
    drop_enc = OneHotEncoder(drop='first').fit([['Male', 1], ['Female', 3], ['Female', 2]])
    print(drop_enc.categories_)
    a = drop_enc.transform([['Female', 1], ['Male', 2]]).toarray()
    print(a)

    # drop a column for feature only having 2 categories:
    drop_binary_enc = OneHotEncoder(drop='if_binary').fit([['Male', 1], ['Female', 3], ['Female', 2]])
    a = drop_binary_enc.transform([['Female', 1], ['Male', 2]]).toarray()
    print(a)

    def custom_combiner(feature, category):
        return str(feature) + "_" + type(category).__name__ + "_" + str(category)
    custom_fnames_enc = OneHotEncoder(feature_name_combiner=custom_combiner).fit([['Male', 1], ['Female', 3], ['Female', 2]])
    a = custom_fnames_enc.get_feature_names_out()
    print(a)

    # Infrequent categories are enabled by setting max_categories or min_frequency.
    import numpy as np
    X = np.array([["a"] * 5 + ["b"] * 20 + ["c"] * 10 + ["d"] * 3], dtype=object).T
    ohe = OneHotEncoder(max_categories=3, sparse_output=False).fit(X)
    print(ohe.infrequent_categories_)
    a = ohe.transform([["a"], ["b"]])
    print(a)


def apiDoc_RandomForestClassifier():
    """
    https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
    """

    from sklearn.ensemble import RandomForestClassifier
    from sklearn.datasets import make_classification

    X, y = make_classification(n_samples=1000, n_features=4, n_informative=2, n_redundant=0, random_state=0, shuffle=False)
    print(X, y, sep='\n')
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    clf.fit(X, y)
    print(clf.predict([[0,0,0,0]]))


def userGuide_RandomForestClassifier():
    """
    https://scikit-learn.org/stable/modules/ensemble.html#forest
    """

    from sklearn.ensemble import RandomForestClassifier
    X = [[0, 0], [1, 1]]
    Y = [0, 1]
    clf = RandomForestClassifier(n_estimators=10)
    clf = clf.fit(X, Y)
    print(clf.predict([[0, 1], [1, 0]]).tolist())



if __name__ == "__main__":
    #userGuide_TrainTestSplit()
    #apiTrainTestSplit()

    #docExample_SimpleImputer()
    #userGuide_SimpleImputer()

    #docExample_OneHotEncoder()

    #apiDoc_RandomForestClassifier()
    userGuide_RandomForestClassifier()
