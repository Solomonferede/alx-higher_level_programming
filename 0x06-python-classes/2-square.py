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

        try:
            if not isinstance(size, int):
                raise TypeError
            elif size < 0:
                raise ValueError
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
