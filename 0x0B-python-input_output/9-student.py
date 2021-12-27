#!/usr/bin/python3
"""The 9-student module
Create a class Student and define a method to retrieve dictionary 
representation of the class
"""


class Student(obj):
    """Defination of student class

    Methods:
        __init__: Initialize the instance atribute
        to_json: return dictionary representation of a class
        """

    def __init__(self, first_name, last_name, age):
        """Initialize the value of instance atribute when created the instance

        args:
            first_name - The first name of the student
            last_name - The last name of the student
            age - Age of the studnt
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self)
    """Method which returns the dictionary representation of a class"""

    return obj.__dic__
