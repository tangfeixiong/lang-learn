#!/usr/bin/env python3

"""
1.17. Neural network models (supervised)

References:
- “Learning representations by back-propagating errors.” Rumelhart, David E., Geoffrey E. Hinton, and Ronald J. Williams.
- “Stochastic Gradient Descent” L. Bottou - Website, 2010.
- “Backpropagation” Andrew Ng, Jiquan Ngiam, Chuan Yu Foo, Yifan Mai, Caroline Suen - Website, 2011.
- “Efficient BackProp” Y. LeCun, L. Bottou, G. Orr, K. Müller - In Neural Networks: Tricks of the Trade 1998.
- “Adam: A method for stochastic optimization.” Kingma, Diederik, and Jimmy Ba (2014)

<https://scikit-learn.org/stable/modules/neural_networks_supervised.html>
"""

# 1.17.1. Multi-layer Perceptron

def multi_layer_perceptron() -> None:
    """Multi-layer Perceptron (MLP) is a supervised learning algorithm
    The advantages of Multi-layer Perceptron are:
    . Capability to learn non-linear models
    . Capability to learn models in real-time (on-line learning) using partial_fit
    The disadvantages of Multi-layer Perceptron (MLP) include:
    .MLP with hidden layers have a non-convex loss function where there exists more than one local minimum. Therefore different random weight initializations can lead to different validation accuracy
    .MLP requires tuning a number of hyperparameters such as the number of hidden neurons, layers, and iterations
    .MLP is sensitive to feature scaling"""

    pass

# 1.17.2. Classification

def multi_layer_perceptron_classification() -> None:
    """Class MLPClassifier implements a multi-layer perceptron (MLP) algorithm that trains using Backpropagation"""

    import sklearn

    from sklearn.neural_network import MLPClassifier

    X = [[0., 1.], [1., 1.]]
    y = [0, 1]
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                        hidden_layer_sizes=(5, 2), random_state=1)

    clf.fit(X, y)
    print(clf.predict([[2., 2.], [-1., -2.]]))

    print([coef.shape for coef in clf.coefs_])

    print(clf.predict_proba([[2., 2.], [1., 2.]]))

    X = [[0., 0.], [1., 1.]]
    y = [[0., 0.], [1., 1.]]
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                        hidden_layer_sizes =(15,), random_state=1)
    clf.fit(X, y)
    print(clf.predict([[1., 2.]]))
    print(clf.predict([[0., 0.]]))

# 1.17.3 Regression

def multi_layer_perceptron_regression() -> None:
    """Class MLPRegressor implements a multi-layer perceptron (MLP) that trains using backpropagation with no activation function in the output layer, which can also be seen as using the identity function as activation function. Therefore, it uses the square error as the loss function, and the output is a set of continuous values.
    MLPRegressor also supports multi-output regression, in which a sample can have more than one target."""

    pass

# 1.17.4 Regularization

def l2_regularization() -> None
   """Both MLPRegressor and MLPClassifier use parameter alpha for regularization (L2 regularization) term which helps in avoiding overfitting by penalizing weights with large magnitudes"""

    pass

# 1.17.5 Algorithm

def mult_layer_perceptron_algorithm() -> None:
    """MLP trains using Stochastic Gradient Descent, Adam, or L-BFGS. """

    pass

# 1.17.6 Complexity

def multi_layer_perceptron_complexity() -> None:
    """Suppose there are n training samples, m features, k hidden layers, each containing h neurons - for simplicity, and o output neurons. The time complexity of backpropagation is, where  is the number of iterations. Since backpropagation has a high time complexity, it is advisable to start with smaller number of hidden neurons and few hidden layers for training."""

# 1.17.7 Mathematical formulation

def multi_layer_perceptron_mathematical_formulation() -> None:
   """https://scikit-learn.org/stable/modules/neural_networks_supervised.html#mathematical-formulation"""

    pass

# 1.17.8. Tips on Practical Use

def multi_layer_perceptron_practical_tips() -> None:
    """Multi-layer Perceptron is sensitive to feature scaling, so it is highly recommended to scale your data"""

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    # Don't cheat - fit only one training data
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    # apply same transformation to test data
    X_test = scaler.transform(X_test)

# 1.17.9 More control with warm_start

def multi_layer_perceptron_more_control() -> None:
    """If you want more control over stopping criteria or learning rate in SGD, or want to do additional monitoring, using warm_start=True and max_iter=1 and iterating yourself can be helpful"""

    X = [[0., 0.], [1., 1.]]
    y = [0, 1]
    clf = MLPClassifer(
        hidden_layer_sizes=(15,), random_state=1, max_iter=1, warm_start=True
    )
    for i in range(10):
        clf.fit(X, y)
        # additional monitoring / inspection


if __name__ == "__main__":
    classification()   
