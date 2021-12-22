#!/usr/bin/python3
"""1-write_file module.
Define A function that writes string to a text file
"""


def write_file(filename="", text=""):
    """Function defination that writes on text file

    Args:
        - filename - the name of the file
        - text - the text to be write
    returns -the number of character written
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        written_character = f.write(text)
    return written_character
