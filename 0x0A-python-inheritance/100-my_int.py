#!/usr/bin/python3
"""
100-my_int.py
"""


class MyInt(int):
    """ Class that inherits form int """
    def __init__(self, value):
        self.value = value
    """ change the value"""
    def __eq__(self, other):
        return self.value != other
    """ change te value"""
    def __ne__(self, other):
        return self.value == other
