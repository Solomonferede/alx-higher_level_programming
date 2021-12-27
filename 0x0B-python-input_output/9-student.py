#!/usr/bin/python3
""" The 9-student module
Create a class Student with public instance atribute and
initialize the value 
It define a method to retrieve dictionary representation
of the class
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
    """define a method which returns the dictionary representation of a class"""

    return obj.__dic__
