#!/usr/bin/env python3

import numpy as np
from scipy.sparse import csc_array

def docExample_CompressedSparseColumnMatrix():
    """
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csc_matrix.html
    """

    a = csc_array((3, 4), dtype=np.int8).toarray()
    print(repr(a))

    row = np.array([0, 2, 2, 0, 1, 2])
    col = np.array([0, 0, 1, 2, 2, 2])
    data = np.array([1, 2, 3, 4, 5, 6])
    m = csc_array((data, (row, col)), shape=(3, 3))
    a = m.toarray()
    print(repr(a))
    print(m.getrow(2))

    indptr = np.array([0, 2, 3, 6])
    indices = np.array([0, 2, 2, 0, 1, 2])
    data = np.array([1, 2, 3, 4, 5, 6])
    a = csc_array((data, indices, indptr), shape=(3, 3)).toarray()
    print(repr(a))


if __name__ == "__main__":
    docExample_CompressedSparseColumnMatrix()
