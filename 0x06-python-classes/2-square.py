#!/usr/bin/python3
"""Square module:
     that defines a square.

"""


class Square:
    """Define a class square

    Methods:
        __init__: initialize the atributes

    """

    def __init__(self, size=0):
        """Initializing The atribute"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
