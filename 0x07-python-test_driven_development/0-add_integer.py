#!/usr/bin/bash
"""module 0-add_integer
Define integer addation function
"""


def add_integer(a, b=98):
    """Define add_integer funnction"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
