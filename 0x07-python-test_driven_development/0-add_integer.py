#!/usr/bin/python3
"""
0-add_integer.py file
Functions:
-> add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """
        Adds two integers (a and b)
    """

    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
