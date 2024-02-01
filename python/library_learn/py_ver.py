#!/usr/bin/env python3

"""
    Check Python version on command line and in script
    <https://note.nkmk.me/en/python-sys-platform-version-info/>
"""

import sys
import platform

def about_py_vers() -> None:
    """ https://note.nkmk.me/en/python-sys-platform-version-info/#check-the-python-version-in-a-script-sys-platform """

    print("sys.version type:", type(sys.version))
    print(sys.version)

    print("sys.version_info type:", type(sys.version_info))
    print(sys.version_info)

    print("major:", sys.version_info.major)
    if sys.version_info[0] == 3:
        print('Python3')
    else:
        print('Python2')

    v = platform.python_version()
    print("platform.python_version() return:", type(v))
    print(v)
    ver = platform.python_version_tuple()
    print("platform.python_version_tuple() return:", type(ver))
    print(ver)

if __name__ == "__main__":
    about_py_vers()

