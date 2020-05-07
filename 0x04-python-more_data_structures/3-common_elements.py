#!/usr/bin/python3
def common_elements(set_1, set_2):
    commons = []
    for el1 in set_1:
        for el2 in set_2:
            if el1 == el2:
                commons.append(el1)
    return commons
