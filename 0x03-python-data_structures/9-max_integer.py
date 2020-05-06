#!/usr/bin/python3
def max_integer(l=[]):
    if len(l) is 0:
        return None
    return sorted(l)[-1]
