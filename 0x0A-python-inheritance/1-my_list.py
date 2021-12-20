#!/usr/bin/python3
"""Module 1-my_list.py:
print a list in ascending order.
"""


class MyList(list):
    """defining a class of MyList inherited from class list"""

    def print_sorted(self):
        """Define a method that prints a list in sorted order"""
        new_list = self[:]
        new_list.sort()
        print(new_list)
