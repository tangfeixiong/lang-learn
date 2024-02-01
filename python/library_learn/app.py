#!/usr/bin/env python3

"""
    https://docs.python.org/3.12/library/__main__.html#idiomatic-usage
"""

import sys

def usage() -> None:
    info = '''Usage:
    `python3 -m library_learn.main <name> <argv>`
or
    `python3 <path>/<to>/library_learn <name> <argv>`
    '''
    print(info)

def main() -> object:
    if len(sys.argv) == 1:
        usage()
        return 0

    if sys.argv[1] == "command-line-args":
        return NotImplemented

    print(sys.argv)
    return 1
    

if __name__ == "__main__":
    sys.exit(main())




