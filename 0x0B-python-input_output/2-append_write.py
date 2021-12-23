#!/usr/bin/python3
"""The 2-append_write Module
Represent a function that append the exiting file
"""


def append_write(filename="", text=""):
    """Define the function that append file

    Args:
        filename - name of the file
        text - the text to be written
    returns: The number of character written.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        character_write = f.write(text)
        return character_write
