#!/usr/bin/python3
"""
2-read_lines.py
"""


def read_lines(filename="", nb_lines=0):
    """ read the lines of a file"""
    with open(filename, encoding='uft8') as f:
        if nb_lines <= 0:
            for ln in f:
                print(ln, end='')
        else:
            for ln in range(nb_lines):
                print(f.readline(), end='')
