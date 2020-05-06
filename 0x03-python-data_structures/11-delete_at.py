#!/usr/bin/python3
def delete_at(lis=[], i=0):
    if i < 0 or i >= len(lis):
        return lis
    del lis[i]
    return (lis)
