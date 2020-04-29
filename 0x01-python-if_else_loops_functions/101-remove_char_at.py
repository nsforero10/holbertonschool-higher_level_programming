#!/usr/bin/python3
def remove_char_at(str, n):
    cp = ''
    for i in range(0, len(str)):
        if i != n:
            cp += str[i]
    return cp
