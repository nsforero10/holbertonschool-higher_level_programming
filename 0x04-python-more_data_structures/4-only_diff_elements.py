#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = []
    for el1 in set_1:
        if el1 not in set_2:
            diff.append(el1)
    for el2 in set_2:
        if el2 not in set_1:
            diff.append(el2)
    return diff
