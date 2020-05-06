#!/usr/bin/python3
def print_matrix_integer(m=[[]]):
    print('\n'.join(
        [' '.join(['{:d}'.format(i)for i in r])for r in m]
    ))
