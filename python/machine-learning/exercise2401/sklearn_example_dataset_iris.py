#!/usr/bin/env python3

"""
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris
"""

import matplotlib.pyplot as plt
# unused but required import for doing 3D projections with matplotlib < 3.2
import mpl_toolkits.mplot3d # noqa: F401
import numpy as np

from sklearn import datasets, decomposition

iris = datasets.load_iris()

# The Iris Dataset

def sepal_visualize() -> None:
    """https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
    This data sets consists of 3 different types of irises’ (Setosa, Versicolour, and Virginica) petal and sepal length, stored in a 150x4 numpy.ndarray

    The rows being the samples and the columns being: Sepal Length, Sepal Width, Petal Length and Petal Width.
"""
    _, ax = plt.subplots()
    scatter = ax.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
    ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
    _ = ax.legend(scatter.legend_elements()[0], iris.target_names, loc="lower right", title="classes")

# PCA example with Iris Data-set

def principal_component_analysis_visualize() -> None:
    """https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html#sphx-glr-download-auto-examples-decomposition-plot-pca-iris-py"""

    np.random.seed(5)

    X = iris.data
    y = iris.target

    fig = plt.figure(1, figsize=(4, 3))
    plt.clf()

    ax = fig.add_subplot(111, projection="3d", elev=48, azim=134)
    ax.set_position([0, 0, 0.95, 1])

    plt.cla()
    pca = decomposition.PCA(n_components=3)
    pca.fit(X)
    X = pca.transform(X)

    for name, label in [("Setoca", 0), ("Versicolour", 1), ("Virginica", 2)]:
        ax.text3D(
            X[y == label, 0].mean(),
            X[y == label, 1].mean() + 1.5,
            X[y == label, 2].mean(),
            name,
            horizontalalignment="center",
            bbox=dict(alpha=0.5, edgecolor="w", facecolor="w"),
        )
    # Reorder the labels to have colors matching the cluster results
    y = np.choose(y, [1, 2, 0]).astype(float)
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.nipy_spectral, edgecolor="k")

    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])
    ax.zaxis.set_ticklabels([])

    plt.show()

def print_info() -> None:
    print(f'{iris.feature_names=}')
    print('feature shape:', iris.data.shape, 'type:', type(iris.data), 'samples:', len(iris.data)) 
    print('head row:', iris.data[0])
    print('targeet names:', list(iris.target_names))
    print('target shape:', iris.target.shape, 'type:', type(iris.target), "examples:", iris.target[[10, 25, 50]])

if __name__ == "__main__":
    print_info()


    #sepal_visualize()
    #plt.show()

    principal_component_analysis_visualize()
