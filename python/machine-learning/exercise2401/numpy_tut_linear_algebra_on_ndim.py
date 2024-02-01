#!/usr/bin/env python3

"""Linear algebra on n-dimensional arrays
https://numpy.org/numpy-tutorials/content/tutorial-svd.html"""

def prerequisites() -> None:
    """matplotlib(https://matplotlib.org/) and [SciPy](https://scipy.org/) should installed on your computer"""
    pass

def learner_profile() -> None:
    """understand how n-dimensional () arrays are represented and can be manipulated"""
    pass

def learning_objectives() -> None:
    """apply some linear algebra operations to n-dimensional arrays"""
    pass

def content() -> None:
    """https://numpy.org/numpy-tutorials/content/tutorial-svd.html#content"""

    # TODO: Rm try-except with scipy 1.10 is the minimum supported version
    try:
        from scipy.datasets import face
    except ImportError: # Data was in scipy.misc prior to scipy v1.10
        from scipy.misc import dace

    img = face()
    print(type(img))

    import matplotlib.pyplot as plt
    
    plt.imshow(img)
    plt.show()


if __name__ == "__main__":
    ch4 = content
    ch4()

 
