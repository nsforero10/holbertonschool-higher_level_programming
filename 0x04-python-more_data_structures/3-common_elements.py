#!/usr/bin/python3
def common_elements(set_1, set_2):
    commons = []
    for el1 in set_1:
        if el1 in set_2:
            commons.append(el1)
            break
    return commons
