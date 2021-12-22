#!/usr/bin/python3
"""0-read_file module
Define a function to read a text file
"""


def read_file(filename=""):
    """define a read_file function.

    args:
        - filename: the name of the file to be read
    
    """

    with open(filename, mode = 'r', encoding = 'utf-8') as f:
        file_read = f.read()
    print(file_read)

