#!/usr/bin/python3
"""
file: 1-mi_list.py
"""


class MyList(list):
    """ a class that inherits from a list """
    def print_sorted(self):
        """ prints sorted lists """
        print(sorted(self))
