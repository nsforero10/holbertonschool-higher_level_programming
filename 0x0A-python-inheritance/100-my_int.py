#!/usr/bin/python3
"""
100-my_int.py
"""


class MyInt(int):
    """ Class that inherits form int """
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        """ change the value"""
        return self.value != other

    def __ne__(self, other):
        """ change te value"""
        return self.value == other
