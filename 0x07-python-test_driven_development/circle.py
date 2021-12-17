from math import pi

def circle_area(r):
    if r < 0:
        raise ValueError("The radius cant be negative number")
    return pi * r ** 2
