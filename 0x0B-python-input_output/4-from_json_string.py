#!/usr/bin/python3
"""The 4-from_json_string module
Change the json object to string
"""
import json


def from_json_string(my_str):
    """Define a function to change json to string.

    Args:
        my_str - json string

    return -return object of json string
    """

    return json.loads(my_str)
