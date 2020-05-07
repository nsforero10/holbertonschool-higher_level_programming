#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_set = set(my_list)
    count = 0
    for el in uniq_set:
        count += el
    return count
