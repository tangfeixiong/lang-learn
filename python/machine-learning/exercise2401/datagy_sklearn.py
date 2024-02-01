#!/usr/bin/env python3

# Splitting Your Dataset    
def dataProcess_sklearnTrainTestSplit():
    """
    https://datagy.io/sklearn-train-test-split/
    """

    # Loading the wine dataset from sklearn
    from sklearn.datasets import load_wine
    from sklearn.model_selection import train_test_split

    wine = load_wine()
    print(wine.DESCR)
    X = wine.data
    y = wine.target

    # Using train_test_split to Split Data into Training and Testing Data
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y,
            test_size=0.3, random_state=100, stratify=y)
    print("\n\n", y, "\n\n", y_train, "\n\n", y_test, "\n\n")
    '''
    # Returning a Non-Stratified Result
    X_train, X_test, y_train, y_test = train_test_split(X, y,
            test_size=0.3, random_state=100, shuffle=True)
    print("\n\n", y, "\n\n", y_train, "\n\n", y_test, "\n\n")

    import pandas as pd
    df = pd.DataFrame(y)
    print(df.value_counts())

    # Seeing the split across training and testing datasets
    print('Number of records in the original dataset: ', len(y))
    print('Number of records in the training dataset: ', len(y_train))
    print('Number of records in the testing dataset: ', len(y_test))
    
    # Generate a Two Column DataFrame
    import matplotlib.pyplot as plt
    import seaborn as sns

    data = pd.DataFrame(X)
    df = pd.DataFrame()
    df['Features'] = data[0]
    df['Targets'] = y
    print(df.head())

    # Split and Label the Data
    df_train, df_test = train_test_split(df)
    df_train['Type'] = 'Train'
    df_test['Type'] = 'Test'
    print(df_train.head(), df_test.head(), sep='\n')

    # Combine the Data
    '''
    final_df = df_train.append(df_test)
    '''
    final_df = pd.concat([df_train, df_test], ignore_index=True)
    print(final_df)

    # Visualize the Data
    sns.set_style('darkgrid')
    sns.set_palette('pastel')
    sns.catplot(data=final_df, x='Targets', y='Features', hue='Type')
    plt.show()


# One-Hot Encoding
def dataPreprocess_sklearnOneHotEncoder():
    """
    https://datagy.io/sklearn-one-hot-encode/
    """
    
    # One-hot encoding a single column column
    from sklearn.preprocessing import OneHotEncoder
    from seaborn import load_dataset

    df = load_dataset('penguins')
    print(df.loc[:, ['island']].head(32))
    ohe = OneHotEncoder()
    transformed = ohe.fit_transform(df[['island']])
    print(transformed.toarray()[:32])

    # Getting one hot encoded categories
    print(ohe.categories_)

    df[ohe.categories_[0]] = transformed.toarray()
    print(df.head())
    
   
def dataPreprocess_sklearnMakeColumnTransformer():
    """ How to Use ColumnTransformer with OneHotEncoder """

    # Using make_column_transformer to One-Host encoder
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.compose import make_column_transformer
    from seaborn import load_dataset
    import pandas as pd

    df = load_dataset('penguins')

    transformer = make_column_transformer((OneHotEncoder(), ['island']), remainder='passthrough')
    transformed = transformer.fit_transform(df)
    transformed_df = pd.DataFrame(transformed, columns=transformer.get_feature_names_out())
    print(transformed_df.head())


def dataPreprocess_sklearnOneHotEncoder_transformMultiCols():
    """ One-Hot Encode Multiple Columns with Scikit-Learn """ 

    from sklearn.preprocessing import OneHotEncoder
    from sklearn.compose import make_column_transformer
    from seaborn import load_dataset
    import pandas as pd

    df = load_dataset('penguins')
    df = df[['island', 'sex', 'body_mass_g']]
    df = df.dropna()

    transformer = make_column_transformer((OneHotEncoder(), ['island', 'sex']), remainder='passthrough')

    transformed = transformer.fit_transform(df)
    transformed_df = pd.DataFrame(transformed, columns=transformer.get_feature_names_out())
    print(transformed_df.head())


# Introduction to Random Forests
def algorithmIntro_skleanRandomForestClassifier():
    """
    https://datagy.io/sklearn-random-forests/
    """
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context

    # Loading the Penguins Dataset from Seaborn
    import seaborn as sns
    import pandas as pd

    df = sns.load_dataset('penguins')
    print(df.head())

    # Displaying Info on the Penguins Dataset
    print(df.info())

    # Seeing missing data
    print(df.isnull().sum())

    # Imputing missing numerical data
    from sklearn.impute import SimpleImputer
    import numpy as np

    # Create a SimpleImputer class
    imputer = SimpleImputer(missing_values=np.NaN, strategy='mean')
    
    # Fit the columns to the object
    columns = ['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g']
    imputer = imputer.fit(df[columns])
    
    # Transform the DataFrames column with the fitted data
    df[columns] = imputer.transform(df[columns])
    print(df[columns])

    # Dropping missing records in the sec column
    df = df.dropna(subset=['sex'])

    # Checking that no missing data exists
    print(df.isnull().sum())

    # Mapping the sex variable to binary values
    df['sex int'] = df['sex'].map({'Male': 0, 'Female': 1})
    print(df['sex int'].head())

    # Checking unique values in the island feature
    print(df['island'].unique())

    # One-hot Encoding the Island Feature
    from sklearn.preprocessing import OneHotEncoder
    one_hot = OneHotEncoder()
    encoded = one_hot.fit_transform(df[['island']])
    df[one_hot.categories_[0]] = encoded.toarray()
    print(df.head())

    # Dropping Unnecessary Columns
    df = df.drop(columns=['island', 'sex'])

    # Creating Your First Random Forest: Classifying Penguins

    # Splitting the data and creating a model
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier

    X = df.iloc[:, 1:]
    y = df['species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=100)

    forest = RandomForestClassifier(n_estimators=100, random_state=100)

    # Fitting a model and making predictions
    forest.fit(X_train, y_train)
    predictions = forest.predict(X_test)

    # Evaluating the model
    from sklearn import metrics
    print("Accuracy:", metrics.accuracy_score(y_test, predictions))


    # Visualizing Random Forest Decision Trees
    import matplotlib.pyplot as plt
    from sklearn.tree import plot_tree

    fig = plt.figure(figsize=(15, 10))
    plot_tree(forest.estimators_[0], feature_names=X.columns, class_names=df['species'].unique(), filled=True, rounded=True)
    plt.show()

    fig = plt.figure(figsize=(15, 7))
    plot_tree(forest.estimators_[11], feature_names=X.columns, class_names=df['species'].unique(), filled=True, rounded=True)
    plt.show()


def algorithmIntro_sklearnDecisionTreeClassifier():
    """
    https://datagy.io/sklearn-decision-tree-classifier/
    """
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context

    # Downloading ad exploring the Titanic dataset
    import pandas as pd
    data = pd.read_csv('https://raw.githubusercontent.com/datagy/data/main/titanic.csv', usecols=['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Fare', 'Embarked'])
    data = data.dropna()
    
    print(data.head())

    # Plotting a Pairplot of Titanic Data
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.pairplot(data=data, hue='Survived')
    plt.show()

    # Loading only numeric columns
    data = pd.read_csv('https://raw.githubusercontent.com/datagy/data/main/titanic.csv', usecols=['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare'])
    data = data.dropna()

    X = data.copy()
    y = X.pop('Survived')

    # Splitting data into training and testing data
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=100)

    # Creating Our First Decision Tree Classifier
    from sklearn.tree import DecisionTreeClassifier
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    # Making Predictions with Our Model
    predictions = clf.predict(X_test)
    print(predictions[:5])

    # Measuring the accuracy of our model
    from sklearn.metrics import accuracy_score
    print(accuracy_score(y_test, predictions))



    #
    # How to Work with Categorical Data in Decision Tree Classifiers
    #

    # Attempting to build a model with non-numerical data
    X = pd.read_csv('https://raw.githubusercontent.com/datagy/data/main/titanic.csv', usecols=['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex', 'Embarked'])
    X = X.dropna()
    y = X.pop('Survived')

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=100)

    # One-Hot encoding our data
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.compose import make_column_transformer

    column_transformer = make_column_transformer((OneHotEncoder(), ['Sex', 'Embarked']), remainder='passthrough')

    X_train = column_transformer.fit_transform(X_train)
    X_train = pd.DataFrame(data=X_train, columns=column_transformer.get_feature_names_out())

    # Making Predictions with One-Hot Encoded Values
    X_test = column_transformer.transform(X_test)
    X_test = pd.DataFrame(data=X_test, columns=column_transformer.get_feature_names_out())

    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    predictions = clf.predict(X_test)
    print(accuracy_score(y_test, predictions))

    #
    # Hyperparameter Tuning for Decision Tree Classifiers
    #

    # Creating a dictionary of parameters to use in GridSearchCV
    from sklearn.model_selection import GridSearchCV

    params ={'criterion': ['gini', 'entropy'], 'max_depth': [None, 2, 4, 6, 8, 10], 'max_features': [None, 'sqrt', 'log2', 0.2, 0.4, 0.6, 0.8], 'splitter': ['best', 'random']}
    clf = GridSearchCV(estimator=DecisionTreeClassifier(), param_grid=params, cv=5, n_jobs=5, verbose=1,)
    
    clf.fit(X_train, y_train)
    print(clf.best_params_)

    # Using the Parameters from GridSerarchCV
    clf = DecisionTreeClassifier(max_depth=4, criterion='entropy', max_features=0.6, splitter='best')
    clf.fit(X_train, y_train)
    prediction = clf.predict(X_test)

    print(accuracy_score(y_test, predictions))



if __name__ == "__main__":
    #dataProcess_sklearnTrainTestSplit()
    
    #dataPreprocess_sklearnOneHotEncoder()
    #dataPreprocess_sklearnMakeColumnTransformer()
    #dataPreprocess_sklearnOneHotEncoder_transformMultiCols()
    
    #algorithmIntro_skleanRandomForestClassifier()
    algorithmIntro_sklearnDecisionTreeClassifier()    

    #input("press key [enter] to exit!")
