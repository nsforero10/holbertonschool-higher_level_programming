#!/usr/bin/python3
def no_c(my_string):
    noc = []
    [noc.append(char) for char in my_string if char != 'c' and char != 'C']
    noc = ''.join(noc)
    return noc
