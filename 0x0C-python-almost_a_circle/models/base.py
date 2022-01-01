#!/usr/bin/python3
"""The base module
Define a class Base that initialize and has has 1 private atribute.
"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """It return the json string representation of list dictionary"""

        if list_dictionaries is None or list_dictionaries == []:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file:"""
        
        file_name = cls.__name__ + ".json"
        json_string = cls.to_json_string([list.to_dictionary() for list in list_objs])
        with open(file_name, mode='w', encoding='utf-8') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """It recieve json string representation as argument 
        and Returns the equivalent list:"""

        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

