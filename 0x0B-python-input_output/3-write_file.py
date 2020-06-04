#!/usr/bin/python3
"""
2-write_file.py
"""


def append_write(filename="", text=""):
    """ writes the text in a file"""
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
