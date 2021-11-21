#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list)
    if idx < 0 or idx >= size:
        new_list = None
    else:
        new_list = my_list.pop(idx)
    return new_list
