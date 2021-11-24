#!/usr/bin/python3
def max_integer(my_list=[]):
    size = len(my_list)
    if size == 0:
        max = None
    else:
        max = 0
        for value in my_list:
            if max < value:
                max = value
    return max
