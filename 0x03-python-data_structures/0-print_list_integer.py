#!/usr/bin/python3
def print_list_integer(my_list=[]):
    max = len(my_list)
    for i in range(max):
        print("{:d}".format(my_list[i]))
