#!/usr/bin/env python3

# Method 1: Check if a File or Directory Exists in Python using os.path.exists()

def file_exists() -> None:
    # importing os module
    import os

    # specify path
    path = '/usr/local/bin/'

    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    print(isExist)

    # Specify path
    path = '/home/User/Desktop/file.txt'

    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    print(isExist)

# Method 2: Check if a File or Directory Exists in Python using os.path.isfile()

def verify_file() -> None:
    # importing os module
    import os

    # path
    path = '/usr/bin/uname'

    # Check whether the specified path is an existing file
    isFile = os.path.isfile(path)
    print(isFile)

    # path
    path = '/usr/bin'

    # Check whether the specified path is an existing file
    isFile = os.path.isfile(path)
    print(isFile)

# Method 3: Check if a File or Directory Exists in Python using os.path.isdir()

def verify_dir() -> None:
    # importing os.path module
    import os

    # Path
    path = '/usr/bin/uname'

    # Check whether the specified path is an existing directory or not
    isdir = os.path.isdir(path)
    print(isdir)

    # Path
    path = '/usr/bin'

    # Check whether the specified path is an existing directory or not
    isdir = os.path.isdir(path)
    print(isdir)

if  __name__ == "__main__":
    file_exists()
    verify_file()
    verify_dir()
