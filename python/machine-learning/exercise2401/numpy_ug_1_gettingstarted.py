#!/usr/bin/env python3

"""
Getting started
<https://numpy.org/doc/stable/user/index.html>
"""

import sys
import numpy as np
from numpy import pi
from numpy import newaxis
import matplotlib.pyplot as plt

def what_is():
    """https://numpy.org/doc/stable/user/whatisnumpy.html"""

    pass

def installation()
    """https://numpy.org/install/"""

    pass

def quick_start():
    """https://numpy.org/devdocs/user/quickstart.html"""

    # https://numpy.org/devdocs/user/quickstart.html#the-basics
    print("# https://numpy.org/devdocs/user/quickstart.html#an-example")
    a = np.arange(15).reshape(3, 5)
    print(repr(a))
    print(f'{a.shape=}, {a.ndim=}, {a.size=}')
    print(f'{a.dtype.name=}, {a.itemsize=}, type={type(a)}')

    b = np.array([6, 7, 8])
    print(repr(b), type(b), end='\n\n')

    # https://numpy.org/devdocs/user/quickstart.html#array-creation
    a = np.array([2, 3, 4])
    print(f'{a!r}, {a.dtype=}')
    try:
        a = np.array(1, 2, 3, 4)
    except Exception as err:
        print(type(err).__name__, err)
    a = np.array([1, 2, 3, 4,])
    print(repr(a), a.dtype.name)
    b = np.array([1.2, 3.5, 5.1])
    print(repr(b), b.dtype)

    c = np.array([[1, 2], [3, 4]], dtype=complex)
    print(repr(c))

    print(repr(np.zeros((3, 4))))
    print(repr(np.ones((2, 3, 4), dtype=np.int16)))
    print(repr(np.empty((2, 3))))

    print(np.arange(10, 30, 5))
    print(np.arange(0, 2, 0.3))

    print(repr(np.linspace(0, 2, 9))) # 9 numbers from 0 to 2
    x = np.linspace(0, 2*pi, 100) # useful to evaluate function at lots of points
    f = np.sin(x)
    print(x, f, sep="\n", end="\n\n")

    # https://numpy.org/devdocs/user/quickstart.html#printing-arrays
    a = np.arange(6)
    print(a)

    b = np.arange(12).reshape(4, 3)
    print(b)

    c = np.arange(24).reshape(2, 3, 4)
    print(c)

    print(np.arange(10000))
    print(np.arange(10000).reshape(100, 100))

    np.set_printoptions(threshold=sys.maxsize)
    np.set_printoptions(threshold=0)

    # https://numpy.org/devdocs/user/quickstart.html#basic-operations
    a = np.array([20, 30, 40, 50])
    b = np.arange(4)
    print(a, b)
    c = a - b
    print(f'a-b={c}')
    print(f'b*b={b**2}')
    print(f'10*sina(a)={10*np.sin(a)}')
    print(a < 35)

    a = np.array([[1, 1], [0, 1]])
    b = np.array([[2, 0], [3, 4]])
    print(a * b) # elementwise product
    print(a @ b, a.dot(b)) # matrix product # first should be python>=3.5

    rg = np.random.default_rng(1) # create instance of default random number generator
    a = np.ones((2, 3), dtype=int)
    b = rg.random((2, 3))
    a *= 3
    b += a
    try:
        a += b
    except Exception as err:
        print(err)
    finally:
        print(a, b, sep='\n')
    
    a = np.ones(3, dtype=np.int32)
    b = np.linspace(0, pi, 3)
    c = a + b
    print(b.dtype.name, c, c.dtype.name)
    d = np.exp(c * 1j)
    print(d, d.dtype.name)
    
    a = rg.random((2, 3))
    print(a, a.sum(), a.min(), a.max())

    b = np.arange(12).reshape(3, 4)
    print(b.sum(axis=0)) # sum of each column
    print(b.min(axis=1)) # min of each row
    print(b.cumsum(axis=1)) # cumulative sum along each row

    # https://numpy.org/devdocs/user/quickstart.html#universal-functions
    B = np.arange(3)
    print(B, np.exp(B), np.sqrt(B), sep='\n')
    C = np.array([2., -1., 4.])
    print(np.add(B, C))

    # https://numpy.org/devdocs/user/quickstart.html#indexing-slicing-and-iterating
    a = np.arange(10)**3
    print(a)
    print(a[2])
    print(a[2:5])
    a[:6:2] = 1000 # from start to position 6, exclusive, set every 2nd element to 1000
    print(a)
    print(a[::-1]) # reversed a
    for i in a:
        print(i**(1/3.))

    def f(x, y):
        return 10 * x + y
    b = np.fromfunction(f, (5, 4), dtype=int)
    print(b)
    print(b[2, 3])
    print(b[0:5, 1]) # each row in the second column of b
    print(b[:, 1]) # equivalent to the previous example
    print(b[1:3, :]) # each column in the second and third row of b

    print(b[-1]) # the last row. Equivalent to b[-1, :]

    c = np.array([[[0, 1, 2], [10, 12, 13]], [[100, 101, 102], [110, 112, 113]]]) # a 3D array (two stacked 2D arrays)
    print(c.shape)
    print(c[1, ...]) # same as c[1, :, :] or c[1]
    print(c[..., 2]) # same as c[:, :, 2]

    for row in b:
        print(row)
    
    for element in b.flat:
        print(element)


    # https://numpy.org/devdocs/user/quickstart.html#shape-manipulation
    
    print('# https://numpy.org/devdocs/user/quickstart.html#changing-the-shape-of-an-array')
    a = np.floor(10 * rg.random((3, 4)))
    print(repr(a), a.shape)
    print(a.ravel()) # returns the array, flattend
    print(a.reshape(6, 2)) # returns the array with modified shape
    print(f'{a.T=}, {a.T.shape=}, {a.shape=}') # returns the array, transposed

    a.resize((2, 6))
    print(a)
    print(a.reshape(3, -1))

    print('# https://numpy.org/devdocs/user/quickstart.html#stacking-together-different-arrays')
    a = np.floor(10 * rg.random((2, 2)))
    b = np.floor(10 * rg.random((2, 2)))
    print(a, b, np.vstack((a, b)), np.hstack((a, b)), sep='\n')
    
    print(np.column_stack((a, b))) # with 2D arrays
    a = np.array([4., 2.])
    b = np.array([3., 8.])
    print(np.column_stack((a, b))) # return a 2D array
    print(np.hstack((a, b))) # the result is different
    print(a[:, newaxis]) # view `a` as a 2D column vector
    print(np.column_stack((a[:, newaxis], b[:, newaxis])))
    print(np.hstack((a[:, newaxis], b[:, newaxis]))) # the result is the same

    print(np.r_[1:4, 0, 4])

    print('# https://numpy.org/devdocs/user/quickstart.html#splitting-one-array-into-several-smaller-ones')
    a = np.floor(10 * rg.random((2, 12)))
    print(a)
    print(np.hsplit(a, 3)) # Split `a` into 3
    print(np.hsplit(a, (3, 4))) # Split `a` after the third and the fourth column

    # https://numpy.org/devdocs/user/quickstart.html#copies-and-views'
    print('# https://numpy.org/devdocs/user/quickstart.html#no-copy-at-all')
    a = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
    b = a # no new object is created
    print(b is a) # a and b are two names for the same ndarray object
    
    def f(x):
        print(id(x))

    print(id(a)) # id is a unique identifier of a object
    f(a)

    print('# https://numpy.org/devdocs/user/quickstart.html#view-or-shallow-copy')
    c = a.view()
    print(c is a)
    print(c.base is a) # c is a view of the data owned by a
    print(f'{c.flags.owndata=}')
    
    c = c.reshape((2, 6)) # a's shape doesn't change
    print(f'{a.shape=}')
    c[0, 4] = 1234 # a's data changes
    print(a)

    s = a[:, 1:3]
    s[:] = 10 # s[:] is a view of s. Note the different between s = 10 and s[:] = 10
    print(a)

    print('# https://numpy.org/devdocs/user/quickstart.html#deep-copy')
    d = a.copy() # a new array object with new data is created
    print(d is a)
    print(d.base is a)
    d[0, 0] = 9999
    print(a)

    a = np.arange(int(1e8))
    b = a[:100].copy()
    del a # the memory of ``a`` can be released
    print('a' in locals())

    # https://numpy.org/devdocs/user/quickstart.html#advanced-indexing-and-index-tricks
    print('# https://numpy.org/devdocs/user/quickstart.html#indexing-with-arrays-of-indices')
    a = np.arange(12)**2 # the first 12 square numbers
    i = np.array([1, 1, 3, 8, 5]) # an array of indices
    print(a[i]) # the elements of `a` at the position `i`
    
    j = np.array([[3, 4], [9, 7]]) # a bidimentional array of indices
    print(a[j]) # the same shape as `j`
   
    palette = np.array([[0, 0, 0],        # black
                        [255, 0, 0],      # red
                        [0, 255, 0],      # green
                        [0, 0, 255],      # blue
                        [255, 255, 255]]) # white
    image = np.array([[0, 1, 2, 0], [0, 3, 4, 0]]) # each value corresponds to a color in the palette
    print(palette[image]) # the (2, 4, 3) color image

    a = np.arange(12).reshape(3, 4)
    print(a)
    i = np.array([[0, 1], [1, 2]]) # indices for the first dim of `a`
    j = np.array([[2, 1], [3, 3]]) # indices for the second dim
    print(a[i, j]) # i and j must have equal shape
    print(a[i, 2])
    print(a[:, j])

    l = (i, j)
    print(a[l]) # equialent to a[i, j]
   
    s = np.array([i, j])
    try:
        print(a[s]) # not what we want
    except Exception as err:
        print(err)
    print(a[tuple(s)]) # same as `a[i, j]`

    time = np.linspace(20, 145, 5) # time scale
    data = np.sin(np.arange(20)).reshape(5, 4) # 4 time-dependent series
    print(f'{time=}', f'{data=}', sep='\n')
    ind = data.argmax(axis=0) # index of the maxima for each series
    print(ind)
    time_max = time[ind]
    data_max = data[ind, range(data.shape[1])] # => data[ind[0], 0], data[ind[1], 1]...
    print(time_max)
    print(data_max)
    print(np.all(data_max == data.max(axis=0)))

    a = np.arange(5)
    a[[1, 3, 4]] = 0
    print(a)

    a = np.arange(5)
    a[[0, 0, 2]] = [1, 2, 3]
    print(a)

    a = np.arange(5)
    a[[0, 0, 2]] += 1
    print(a)

    print('# https://numpy.org/devdocs/user/quickstart.html#indexing-with-boolean-arrays')
    a = np.arange(12).reshape(3, 4)
    b = a > 4
    print(b) # `b` is a boolean with `a`'s shape
    print(a[b]) # 1d array with the selected elements
   
    a[b] = 0 # All elements of `a` higher than 4 become 0
    print(a)

    def mandelbrot(h, w, maxit=20, r=2):
        """Returns an image of the Mandelbrot fractal of size (h, w)."""
        x = np.linspace(-2.5, 1.5, 4*h+1)
        y = np.linspace(-1.5, 1.5, 3*w+1)
        A, B = np.meshgrid(x, y)
        C = A + B*1j
        z = np.zeros_like(C)
        divtime = maxit + np.zeros(z.shape, dtype=int)

        for i in range(maxit):
            z = z**2 + C
            diverge = abs(z) > r                  # who is diverging
            div_now =diverge & (divtime == maxit) # who is diverging now    
            divtime[div_now] = i                  # not when
            z[diverge] = r                        # avoid diverging too much

        return divtime

    plt.clf()
    plt.imshow(mandelbrot(400, 400))
    # plt.show()

    a = np.arange(12).reshape(3, 4)
    b1 = np.array([False, True, True]) # first dim selection
    b2 = np.array([True, False, True, False]) # second dim selection

    print(a[b1, :]) # selecting rows
    print(a[b1]) # same thing

    print(a[:, b2]) # selecting columns
    print(a[b1, b2])

    print('# https://numpy.org/devdocs/user/quickstart.html#the-ix-function')
    a = np.array([2, 3, 4, 5])
    b = np.array([8, 5, 4])
    c = np.array([5, 4, 6, 8, 3])
    ax, bx, cx = np.ix_(a, b, c)
    print(ax, bx, cx, sep='\n')
    print(ax.shape, bx.shape, cx.shape)
    result = ax + bx * cx
    print(result)
    print(result[3, 2, 4])
    print(a[3] + b[2] * c[4])

    def ufunc_reduce(ufct, *vectors):
        vs = np.ix_(*vectors)
        r = ufct.identity
        for v in vs:
            r = ufct(r, v)
        return r

    print(ufunc_reduce(np.add, a, b, c))

    # https://numpy.org/devdocs/user/quickstart.html#tricks-and-tips
    print('# https://numpy.org/devdocs/user/quickstart.html#automatic-reshaping')
    a = np.arange(30)
    b = a.reshape((2, -1, 3)) # -1 means "whatever is needed
    print(b.shape)
    print(b)

    print('# https://numpy.org/devdocs/user/quickstart.html#vector-stacking')
    x = np.arange(0, 10, 2)
    y = np.arange(5)
    m = np.vstack([x, y])
    print(m)
    xy = np.hstack([x, y])
    print(xy)

    print('# https://numpy.org/devdocs/user/quickstart.html#histograms')
    rg = np.random.default_rng(1)
    mu, sigma = 2, 0.5 # Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
    v = rg.normal(mu, sigma, 10000)
    plt.figure()
    plt.hist(v, bins=50, density=True) # Plot a normalized histogram with 50 bins
                                       # matplotlib version (plot)
    (n, bins) = np.histogram(v, bins=50, density=True) # Compute the histogram with numpy and then plot it
                                                       # NumPy version (no plot)
    plt.plot(.5 * (bins[1:] + bins[:-1]), n)
    plt.show()

# NumPy: the absolute basics for beginners

# Welcom to NumPy!
def _welcome() -> None:
    """NumPy (Numerical Python) is an open source Python library that’s used in almost every field of science and engineering"""
    pass

# Installing NumPy
def _installing() -> None:
    """If you’re looking for the full instructions for installing NumPy on your operating system, see [Installing NumPy](https://numpy.org/install/)"""
    pass

# How to import NumPy
import numpy as np

# Reading the example code
def _reading_examle_code() -> None:
    a = np.arange(6)
    print(repr(a))
    a2 = a[np.newaxis, :)
    print(ascii(a2))
    print("shape:", a2.shape)

# What's the difference between a Python list and a NumPy array?
def _what_is_difference() -> None:
    """While a Python list can contain different data types within a single list, all of the elements in a NumPy array should be homogeneous"""
    pass

# What is an array?
def _what_is_an_array() -> None:
    print("Initialize from Python lists")
    a = np.array([1, 2, 3, 4, 5, 6])
    print(repr(a))
    print("using nested lists for two- of higher-dimensional data")
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])
    print(ascii(a))
    print(a[10])

# More information aboue arrays
def _more_about_arrays() -> None:
    """A vector is an array with a single dimension (there’s no difference between row and column vectors), while a matrix refers to an array with two dimensions. For 3-D or higher dimensional arrays, the term tensor is also commonly used <https://numpy.org/doc/stable/user/absolute_beginners.html#more-information-about-arrays>"""
    a = np.array([[0., 0., 0.], [1., 1., 1.]])
    print(repr(a))
    print("dimension:", a.shape)

class the_absolute_basics_for_beginners():
    """<https://numpy.org/doc/stable/user/absolute_beginners.html>"""
    
    def welcome() -> None:
        return _welcome(self)

    def installing(self) -> None:
        return _installing()

    def how_to_import(self) -> None:
        pass

    def reading_the_example_code(self) -> None
        return _reading_example_code()

    def what_is_difference(self) -> None:
        return _what_is_difference()
    
    def what_is_an_array(self) -> None:
        return _what_is_an_array()

    def more_about_arrays(self) -> None:
        return _more_about_arrays()

    def create_basic_array(self) -> None:
        pass

    def adding_removing_sorting(self) -> None:
        pass

    def know_shape_and_size(self) -> None:
        pass

    def reshape_array(self) -> None:
        pass

    def convert_1d_to_2d(self) -> None:
        pass

    def indexing_and_slicing(self) -> None:
        pass

    def create_from_existing_data(self) -> None:
        pass

    def basic_array_operation(self) -> None:
        pass

    def broadcasting(self) -> None:
        pass

    def more_useful_operation(self) -> None:
        pass

    def creating_matrices(self) -> None:
        pass

    def generating_random_numbers(self) -> None:
        pass

    def get_unique_items_and_counts(self) -> None:
        pass

    def transposing_and_reshaping_matrix(self) -> None:
        pass

    def reverse_an_array(self) -> None:
        pass

    def reshaping_and_flattening_multidim(self) -> None:
        pass

    def access_docstring(self) -> None:
        pass

    def with_mathematical_formulas(self) -> None:
        pass

    def save_and_load(self) -> None:
        pass

    def importing_exporting_csv(self) -> None:
        pass

    def plotting_with_matplotlib(self) -> None:
        pass


if __name__ == "__main__":
    chapter1 = what_is
    chapter1()
    ch2 = installing
    ch2()
    quick_start()
    ch4 = the_absolute_basics_for_beginners()
