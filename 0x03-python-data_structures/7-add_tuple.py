#!/usr/bin/python3
def add_tuple(tp_a=(), tp_b=()):

    if len(tp_a) is 0:
        tp_a = (0, 0)
    elif len(tuple_a) is 1:
        tp_a = (tp_a[0], 0)
    if len(tp_b) is 0:
        tp_b = (0, 0)
    elif len(tp_b) is 1:
        tp_b = (tuple_b[0], 0)

    return (tp_a[0] + tp_b[0], tp_a[1] + tp_b[1])
