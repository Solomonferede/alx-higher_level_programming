#!/usr/bin/python3
"""7-add_item module
Load from json file add argunments and save to joson file
"""


import os.path
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_list = []
filename = 'add_item.json'

if os.path.exists(filename) and os.path.getsize(filename) > 0:
    my_list = load_from_json_file(filename)

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        my_list.append(arg)

save_to_json_file(my_list, filename)
