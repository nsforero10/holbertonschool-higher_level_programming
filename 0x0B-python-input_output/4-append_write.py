#!/usr/bin/python3
"""
2-write_file.py
"""


def write_file(filename="", text=""):
    """ appends text in a file"""
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
