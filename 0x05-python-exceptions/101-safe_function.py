#!/usr/bin/python3g
from sys import stderr


def safe_function(fct, *args):
    try:
        r = fct(*args)
    except Exception as err:
        r = None
        print("Exception:", err, file=stderr)
    return r
