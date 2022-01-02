#!/usr/bin/python3
"""The base module
Define a class Base that initialize and has has 1 private atribute.
"""


import csv
import os
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

        if json_string is None or json_string == '':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """It returns an instance with all attributes already set:"""

        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from the json file:"""

        filename = cls.__name + '.json'
        l = []
        list_dicts = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                s = f.read()
                list_dicts = cls.from_json_string(s)
                for d in list_dicts:
                    l.append(cls.create(**d))
        return l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs in CSV format
        and saves it to a file.

        Args:
            - list_objs: list of instances
        """

        if (type(list_objs) != list and
           list_objs is not None or
           not all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")

        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file.

        Returns: list of instances
        """

        filename = cls.__name__ + ".csv"
        l = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        l.append(i)
        return l
