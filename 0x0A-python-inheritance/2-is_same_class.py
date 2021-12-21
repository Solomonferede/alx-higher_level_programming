#!/usr/bin/python3
"""the 2-is_same_class.py module
define class returns True if the object is an instance of the specified class;
otherwise False.
"""


def is_same_class(obj, a_class):
    """Define a function is_same_class

    Args:
        - obj - object to look for.
        - a_class - class to verify the instance
    returns: True if obj is an instance of a_class
    """

    return isinstance(obj, a_class)
