# !/usr/bin/python3
"""
100-my-int.py
"""


def add_attribute(obj, name, value):
    """ Adds a attribute to a given object """
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
