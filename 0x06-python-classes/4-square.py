#!/usr/bin/python3
"""Square module:
     that defines a square.

"""


class Square:
    """Define a class square

    Methods:
        __init__: initialize the atributes
        area: determine the area of the square instance
        size: retrive the size

    """

    def __init__(self, size=0):
        """Initializing The atribute"""
        self.__size = size

    @property
    def size(self):
        """define a getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Define a setter method"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Defining the area method"""
        return self.__size ** 2
