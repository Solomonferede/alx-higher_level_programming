#!/usr/bin/python3
"""Square module:
     that defines a square.

"""


class Square:
    """Define a class square

    Methods:
        __init__: initialize the atributes
        area: determine the area of the square instance
        size: set and retrive the private atribute size
        my_print: That prints in stdout the square with the character #


    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializing The atribute"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """define a getter method"""
        return self.__size

    @property
    def position(self):
        """Defining a getter method for __postion"""
        return self.__position

    @position.setter
    def position(self, value):
        """Define Setter method for __postion"""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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

    def my_print(self):
        """Defining my_print method"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " *self.__position[0], end="")
                print('#' * self.__size)
