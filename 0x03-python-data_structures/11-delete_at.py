#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    size = len(my_list)
    if idx < 0 or idx >= size:
        new_list = my_list
    else:
        new_list = my_list
        del new_list[idx]
    return new_list
