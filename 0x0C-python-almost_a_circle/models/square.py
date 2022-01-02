#!/usr/bin/python3
"""the square module define a class Square inherits from
Rectangle
"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining  a Square class inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the atribute by calling the super class Rectangle"""

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Represent the class object as a string"""

        s = "[Square] ({}) {}/{} - {} ".format(
                str(self.id), str(self.x),
                str(self.y), str(self.width))
        return s

    @property
    def size(self):
        """The width method that.
        return the value of private attribute __width.
        """
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the width attribute."""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            self.__height = value

    def update(self, *args, **kwargs):
        """Assign an argument to each atribute"""

        arg_len = len(args)

        if arg_len > 0:
            if arg_len >= 1:
                self.id = args[0]
            if arg_len >= 2:
                self.width = args[1]
                self.height = args[1]
            if arg_len >= 3:
                self.x = args[2]
            if arg_len >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.width = value
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """A function that returns the dictionary representation of a Rectangle"""
        my_dict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return my_dict
