#!/usr/bin/env python3

"""
NumPy fundamentals
https://numpy.org/stable/user/basics.html
"""

import argparse
import os
import sys
import numpy as np

# Array creation

# 1) Converting Python sequences to NumPy Arrays

def converting_python_sequences() -> None:
    """https://numpy.org/doc/stable/user/basics.creation.html#converting-python-sequences-to-numpy-arrays"""

    a1D = np.array([1, 2, 3, 4])
    a2D = np.array([[1, 2], [3, 4]])
    a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(a1D, repr(a2D), ascii(a3D), sep='\n')

    a = np.array([127, 128, 129], dtype=np.int8)
    print(a)

    a = np.array([2, 3, 4], dtype=np.uint32)
    b = np.array([5, 6, 7], dtype=np.uint32)
    c_unsigned32 = a - b
    print('unsigned c:', c_unsigned32, c_unsigned32.dtype)
    c_signed32 = a - b.astype(np.int32)
    print('signed c:', c_signed32, c_signed32.dtype)
    
# 2) Intrinsic NumPy array creation functions

# 1 - 1D array creation functions    
def _1d_array_creation_functions() -> None:
    print(np.arange(10))
    print(np.arange(2, 10, dtype=float))
    print(np.arange(2, 3, 0.1))
    
    print(np.linspace(1., 4., 6))

# 2 - 2D array creation funcitons

def _2d_array_creation_functions() -> None:
    print(np.eye(3))
    print(np.eye(3, 5))

    print(np.diag([1, 2, 3]))
    print(np.diag([1, 2, 3], 1))
    a = np.array([[1, 2], [3, 4]])
    print(a)

    print(np.vander(np.linspace(0, 2, 5), 2))
    print(np.vander([1, 2, 3, 4], 2))
    print(np.vander((1, 2, 3, 5), 4))

# 3 - general ndarray creation functions

def general_ndarray_creation_functions() -> None:
    print(np.zeros((2, 3)))
    print(np.zeros((2, 3, 2)))

    print(np.ones((2, 3)))
    print(np.ones((2, 3, 2)))

    from numpy.random import default_rng
    print(default_rng(42).random((2, 3)))
    print(default_rng(42).random((2, 3, 2)))

    print(np.indices((3, 3)))

def intrinsic_array_creation_functions() -> None:
    """https://numpy.org/doc/stable/user/basics.creation.html#intrinsic-numpy-array-creation-functions"""
    
    _1d_array_creation_functions()
    _2d_array_creation_functions()
    general_ndarray_creation_functions()

# 3) Replicating, joining, or mutating existing arrays

def replicating_joining_mutating() -> None:
    """https://numpy.org/doc/stable/user/basics.creation.html#replicating-joining-or-mutating-existing-arrays"""

    a = np.array([1, 2, 3, 4, 5, 6])
    b = a[:2]
    b += 1
    print('a =', a, '; b =', b)

    a = np.array([1, 2, 3, 4])
    b = a[:2].copy()
    b += 1
    print('a =', a, 'b =', b)

    A = np.ones((2, 2))
    B = np.eye(2, 2)
    C = np.zeros((2, 2))
    D = np.diag((-3, -4))
    print(np.block([[A, B], [C, D]]))

# 4) Reading arrays from disk, either from standard or custom formats

_ug_fundamentals_dir: str = None

def _standard_binary_formats() -> None:
    # Standard Binary Formats
    print('The following lists the ones with known Python libraries to ' +
        'read them and return NumPy arrays (there may be others for which ' + 
        'it is possible to read and convert to NumPy arrays so check the ' +
        'last section as well)')
    print("HDF5: h5py", "FITS: astropy", sep='\n')
    print('Examples of formats that cannot be read directly but for which ' +
        'it is not hard to convert are those formats supported by ' +
        'libraries like PIL (able to read and write many image formats ' +
        'such as jpg, png, etc)')

def _common_ascii_formats() -> None:
    # Common ASCII Formats
    csv = 'simple.csv'
    if _ug_fundamentals_dir is not None:
        csv = os.path.join(_ug_fundamentals_dir, csv)
    print(repr(np.loadtxt(csv, delimiter=',', skiprows=1)))
    print('More generic ASCII files can be read using scipy.io and Pandas')

def reading_from_disk() -> None:
    """https://numpy.org/doc/stable/user/basics.creation.html#reading-arrays-from-disk-either-from-standard-or-custom-formats"""

    _standard_binary_formats()
    _commpn_ascii_formats()

# 5) Creating arrays from raw bytes through the use of strings or buffers

def creating_from_raw_bytes() -> None:
    """https://numpy.org/doc/stable/user/basics.creation.html#creating-arrays-from-raw-bytes-through-the-use-of-strings-or-buffers"""
    print('NumPy fromfile() function and .tofile() method to read and write ' +
        'NumPy arrays directly (mind your byteorder though!) ')
    print('C or C++ library, one can wrap that library with a variety of ' +
        'techniques though that certainly is much more work and requires ' +
        'significantly more advanced knowledge to interface with C or C++')
        
# 6) Use of special library functions (e.g., SciPy, Pandas, and OpenCV)

def use_special_library() -> None:
    """https://numpy.org/doc/stable/user/basics.creation.html#use-of-special-library-functions-e-g-scipy-pandas-and-opencv"""
    print("Many Python libraries, including SciPy, Pandas, and OpenCV, " +
        "use NumPy ndarrays as the common format for data exchange, " +
        "These libraries can create, operate on, and work with NumPy arrays")

class array_creation():
    """https://numpy.org/doc/stable/user/basics.creation.html"""

    # Introduction
    def introduction(self, name: str=None, item: str=None) -> None:
        """There are 6 general mechanisms for creating arrays:
        Conversion from other Python structures (i.e. lists and tuples)
        Intrinsic NumPy array creation functions (e.g. arange, ones, zeros, etc.)
        Replicating, joining, or mutating existing arrays
        Reading arrays from disk, either from standard or custom formats
        Creating arrays from raw bytes through the use of strings or buffers
        Use of special library functions (e.g., random)"""

        name1 = "1) Converting Python sequences to NumPy Arrays".split()
        if ' '.join(name1[1:4]).startswith(name) or \
                '-'.join(name1[1:4]).lower().startswith(name) or \
                '1' == name:
            return converting_python_sequences()
            
        name2 = "2) Intrinsic NumPy array creation functions".split()
        if ' '.join(name2[1:5]).startswith(name) or \
                '-'.join([name2[1], name2[3], name2[4]]).lower().startswith(name) \
                or '2' == name:
            if item is None:
                return intrinsic_array_creation_functions()
            elif item[0] == '1': # 1 - 1D
                return _1d_array_creation_functions()
            elif item[0] == '2': # 2 - 2D
                return _2d_array_creation_functions()
            elif item[0] == '3' or item == 'general': # 3 - general
                return general_ndarray_creation_functions()
            else:
                raise RuntimeError("invalid option of intrinsic creation")
                
        name3 = '3) Replicating, joining, or mutating existing arrays'.split()
        if ' '.join(name3[1:5]).startswith(name) or \
                '-'.join([name3[1], name3[2], name3[4]]).lower().startswith(name) \
                or '3' == name:
            return replicating_joining_mutating()
            
        name4 = '4) Reading arrays from disk, either from standard or custom formats'.split()
        if ' '.join(name4[1:5]).startswith(name) or \
                '-'.join([name4[1], name4[3], name4[4]]).lower().startswith(name) \
                or '4' == name:
            if item is None:
                return reading_from_disk()
            elif item == 'binary':
                return _standard_binary_formats()
            elif item == 'ascii':
                return _common_ascii_formats()
            else:
                raise RuntimeError('Invalid option of reading disk')
                  
        name5 = '5) Creating arrays from raw bytes through the use of strings or buffers'.split()
        if ' '.join(name5[1:6]).startswith(name) or \
                '-'.join([name5[1], name5[3], name5[5]]).lower().startswith(name) \
                or '5' == name:
            return creating_from_raw_bytes()
            
        name6 = '6) Use of special library functions (e.g., SciPy, Pandas, and OpenCV)'.split()
        if ' '.join(name6[1:5]).startswith(name) or \
                '-'.join([name6[1], name6[3], name6[4]]).lower().startswith(name) \
                or '6' == name:
            return use_special_library()
        raise RuntimeError("index must be in range from 1 to 6")

# Indexing on ndarrays

def single_element_indexing() -> None:
    # Single element indexing
    x = np.arange(10)
    print(x[2], x[-2])
    
    a = x.copy()
    x = numpy.reshape(a, (2, 5))
    print(x.shape)
    
    print(x[1, 3], x[1, -1])
    print(ascii(x[0]), x[0][2])
    print('So note that x[0, 2] == x[0][2] though the second case is more ' +
        'inefficient as a new temporary array is created after the first ' +
        'index that is subsequently indexed by 2')
    
class indexing_ndarrays():
    """https://numpy.org/doc/stable/user/basics.indexing.html"""
    
    def basic_indexing(self):
        pass
    def advanced_indexing(self):
        pass
    def field_access(self):
        pass
    def flat_iterator_indexing(self):
        pass
    def assigning_values(self):
        pass
    def dealing_with_variable_numbers(self):
        pass
    def detailed_notes():
        pass


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    _ug_fundamentals_dir = os.path.dirname(script_dir)
    
    parser = argparse.ArgumentParser(
        prog="NumPy User Guide: Fundamentals and Usages",
        description='Understand the fundamental NumPy ideas and philosophy',
        epilog='2024-1-27')
    parser.add_argument('category', type=str, \
        choices=["array-creation", "indexing-ndarrays", 'io'], \
        help='category of learn')
    parser.add_argument('title', type=str, help='title of content')
    parser.add_argument('--item', type=str, help='content item')
    parser.add_argument('--id', type=str, required=False, \
        help='content list')
    args = parser.parse_args()
    if args.category == 'array-creation':
        obj = array_creation()
        if args.title == 'intro':
            sys.exit(obj.introduction(args.item, args.id))
        raise RuntimeError("category not found")
    else:
        sys.exit(NotImplemented)
    
