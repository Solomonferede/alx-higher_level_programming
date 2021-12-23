#!/usr/bin/python3
import json
"""the 3-to_json_string module
Define function that returns the json representation of an object
"""


def to_json_string(my_obj):
    """Defination of a function to_json_string.

    Args:
        my_obj - object to be changed to json string

    Returns - it returns the JSON representation of an object.
    """
    return json.dumps(my_obj)
