#!/usr/bin/python3
"""The base module
Define a class Base that initialize and has has 1 private atribute.
"""


class Base(object):
    """DEfine the Base class

    Methods:
        __init__:initialize the atribute of the instance


    Atributes:
        __nb_objects( int): The number of instances created
        """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the parameter of an instance of the class
        Parametrs:
            id(int): asign the public instance attribute id with this
            argument value
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects