#!/usr/bin/env python3

"""
Command Line Arguments in Python
<https://www.geeksforgeeks.org/command-line-arguments-in-python/>
"""

import sys

# Using sys.argv
# <https://www.geeksforgeeks.org/command-line-arguments-in-python/#sys>

def using_sys_argv() -> None:
    """ Python program to demostrate command line arguments """

    print("# Using sys.argv")
    
    # total arguments
    n = len(sys.argv)
    print("Total arguments passed:", n)

    # Arguments passed
    print("\nName of Python script:", sys.argv[0])

    print("\nArguments passed:", end=" ")
    for i in range(1, n):
        print(sys.argv[i], end=" ")

    print("\n\n# Addition of numbers")
    Sum = 0
    for i in range(1, n):
        try:
            Sum += int(sys.argv[i])
        except ValueError:
            print("skip argument: %s, " % sys.argv[i], end=" ")
    print("\n\nResult:", Sum)

import getopt, sys    

# The Python Standard Library / Generic Operation System Serive
# getopt -- C-style parser for command line options
# <https://docs.python.org/3.12/library/getopt.html>
# Using getopt module
# <https://www.geeksforgeeks.org/command-line-arguments-in-python/#getopt>

def using_getopt_module() -> None:
    """ Python program to demostrate command line arguments """

    print("# Using getopt module")
    # Remove 1st argument from the list of command line arguments
    argumentList = sys.argv[1:]

    # Options
    options = "hmo:"

    # Long options
    long_options = ["Help", "My_file", "Output="]

    try:
        # Parsing arguments
        arguments, values = getopt.getopt(argumentList, options, long_options)
    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))
    else:
        print(arguments, values, sep='\n')
        # checking each argument
        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--help"):
                print("Displaying Help")
            elif currentArgument in ("-m", "--My_file"):
                print("Displaying file_name:", sys.argv[0])
            elif currentArgument in ("-o", "--Output"):
                print("Enabling special output mode (% s)" % (currentValue))

        if len(values) > 0:
            print("Available command arguments:", values)

# The Python Standard Library / Generic Operating System Service
# argparse -- Parser for command-line options, arguments and subcommands
# <https://docs.python.org/3.12/library/argparse.html>
# Using argparse module
# <https://www.geeksforgeeks.org/command-line-arguments-in-python/#argparse>

import argparse

def using_argparse_module() -> None:
    """ Python program to demostate command line arguments """

    print("#Using argparse module")

    msg = "A description of the program"

    # Initialize parser
    parser = argparse.ArgumentParser(description = msg)

    # Adding optional argument
    parser.add_argument("-o", "--Output", help="Show Output",
                        nargs="*", required=False)
    parser.add_argument("-m", "--My_file", help="Display my file",
                        action="store_true", required=False)

    # Read arguments from command line
    args = parser.parse_args()
    print(args)

    if args.Output:
        print("Displaying Output as: % s" % args.Output)
    if args.My_file:
        print("Dispalying my file: %s" % sys.argv[0])


if __name__ == "__main__":
   using_sys_argv()
   using_getopt_module()
   using_argparse_module()

    
