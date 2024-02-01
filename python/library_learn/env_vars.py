#!/usr/bin/env python3

"""
    Using Environment Variables in Python
    <https://datagy.io/python-environment-variables/>
"""

import os

def using_os_environ() -> None:
    """ The easiest way to get all the environment variables available is to print out the os.environ attribute """

    # Getting All Environment Variables Using os
    print(os.environ)

    # Checking the Type of the os.environ
    print(type(os.environ))

    # Getting a Single Environment Variable in Python
    print(os.environ['USER'])

    # Getting an Environment Variable that Doesn't Exist
    try:
        print(os.environ['nonesense'])
    except KeyError:
        print('not exists var: nonesense')

    # Returning None if No Environment Variable Exists
    print(os.getenv('nonesense'))

    # Checking if an Environment Variable Exists in Python
    if 'USER' in os.environ:
         print('Environment variable exists!')
    else:
         print('Environment variable does not exist.')

    # Returning a Default Value When a Variable Doesn't Exist
    print(os.getenv('nonesense', 'default value'))


# pip3 install python-dotenv
# touch <working dir>/.env

from dotenv import load_dotenv

def using_dotenv(envdir :str=None) -> None:
    """ How to Use dotenv in Python to Work with Environment Variables in Python """

    # Loading an Environment Variable File with dotenv
    load_dotenv()

    if envdir:
        load_dotenv()

    print(os.environ)


if __name__ == "__main__":
    using_os_environ()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(__file__, dir_path, sep='\n')

    using_dotenv(os.path.dirname(dir_path))

    
