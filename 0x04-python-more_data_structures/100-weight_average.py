#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sc = 0
        weight = 0
        for elem in my_list:
            sc += elem[0] * elem[1]
            weight += elem[1]
        return sc / weight
    return 0
