#!/usr/bin/python3
def replace_in_list(lis, idx, elem):
    if idx < 0 or idx >= len(lis):
        return lis
    lis[idx] = elem
    return lis
