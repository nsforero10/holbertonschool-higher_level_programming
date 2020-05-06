#!/usr/bin/python3
def print_reversed_list_integer(lis=[]):
    if lis:
        lis.reverse()
        for elem in lis:
            print('{:d}'.format(elem))
