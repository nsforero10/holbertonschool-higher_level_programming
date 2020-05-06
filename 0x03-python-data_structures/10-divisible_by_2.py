#!/usr/bin/python3
def divisible_by_2(lis=[]):
    evens = lis
    for i in range(len(evens)):
        if evens[i] % 2 is 0:
            evens[i] = True
        else:
            evens[i] = False
    return evens
