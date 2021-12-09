#!/usr/bin/python3
""" square module:

    define a class Square.

    """
class Square:
    """Represents a square.

    methods:
        __init__: initialize the atribute.

    """

    def __init__(self, size):
        """Initializes the data.
            
            args:
                size(int): the size of side of the square
        """

        self.__size = size
