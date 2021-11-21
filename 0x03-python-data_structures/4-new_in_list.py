#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list)
    new_list = []
    for i in range(size):
        new_list.append(my_list[i])
    if idx < size and idx >= 0:
        new_list.pop(idx)
        new_list.insert(idx, element)
    return new_list
