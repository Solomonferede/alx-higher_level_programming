#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list)
    if idx < 0 or idx >= size:
        return_value = None
    else:
        return_value = my_list.index(idx)
    return return_value
