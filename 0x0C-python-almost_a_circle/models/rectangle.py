#!/usr/bin/python3
"""The rectangle module
Define a class rectangle inherited from Base class.
"""
from models.base import Base


class Rectangle(Base):
    """Define a class Rectangle

    Methods:
        __init__(): Initialize the class atribute
        width(): get and set the width of the rectangle
        height(): Set and get the height of the rectangle
        x() - set and get private atribute x
        y() - set and get the private atribute y.

    Atributes:
        """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Defining __init__ method.

        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """The width method that.
        return the value of private attribute __width.
        """
        return self.__width

    @width.setter
    def width(self):
        """Set the value of __width"""

        self.__width = width

    @property
    def height(self):
        """The height method that.
        return the value of private attribute __height.
        """
        return self.__height

    @height.setter
    def height(self):
        """Set the value of __width"""

        self.__height = height

    @property
    def x(self):
        """"Return the value of the private atribute __x"""

        return self.__x

    @x.setter
    def x(self):
        """Set the value of __x"""

        self.__x = x

    @property
    def y(self):
        """Return the value of the private atribute __y"""

        return self.__y

    @y.setter
    def y(self):
        """Set the value of __y"""

        self.__y = y
