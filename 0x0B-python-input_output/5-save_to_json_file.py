#!/usr/bin/python3
"""the 5-save_to_json_file module
The module to write an object to a file using json representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Defining save_to_json_file function that write

    Args:
        my_obj - the object to be written
        filename - name of the file
    """

    json_obj = json.dumps(my_obj)
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json_obj)
