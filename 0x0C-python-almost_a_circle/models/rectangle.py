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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The width method that.
        return the value of private attribute __width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute."""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The height method that.
        return the value of private attribute __height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of __height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def x(self):
        """"Return the value of the private atribute __x"""

        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of __x"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Return the value of the private atribute __y"""

        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of __y"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
                self.__y = value

    def __str__(self):
        """Represent the class object as a string"""

        s = "[Rectangle] ({}) {}/{} - {}/{} ".format(
                str(self.id), str(self.__x),
                str(self.__y), str(self.__width),
                str(self.__height))
        return s

    def area(self):
        """Compute and return the area of a rectangle"""

        return (self.__width * self.__height)

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""

        for H in range(self.__height):
            print(self.__width * '#')

    def display(self):
        """Display the Rectangle instance with #"""

        for down in range(self.__y):
            print("\n", end="")
        for H in range(self.__height):
            print(self.__x * " ", end="")
            print(self.__width * '#')

    def update(self, *args, **kwargs):
        """Assign an argument to each atribute"""

        arg_len = len(args)

        if arg_len > 0:
            if arg_len >= 1:
                self.id = args[0]
            if arg_len >= 2:
                self.width = args[1]
            if arg_len >= 3:
                self.height = args[2]
            if arg_len >= 4:
                self.x = args[3]
            if arg_len >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """A function that returns the dictionary representation of a Rectangle"""
        my_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict

