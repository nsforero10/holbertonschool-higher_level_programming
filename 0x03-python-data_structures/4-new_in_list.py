#!/usr/bin/python3
def new_in_list(lis, i, elem):
    newl = list(lis)
    if i < 0 or i >= len(newl):
        return newl
    newl[i] = elem
    return newl
