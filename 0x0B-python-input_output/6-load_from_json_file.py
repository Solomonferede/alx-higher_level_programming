#!/usr/bin/python3
""" the 6-load_from_json_file.py module
Define a function that create an object from json file.
"""
import json


def load_from_json_file(filename):
    """the load_from_json function define

    Args:
        filename - name of the file
    """

    with open(filename, mode='r', encoding='utf-8') as f:
        my_obj = json.load(filename)
        print(my_obj, end="")
