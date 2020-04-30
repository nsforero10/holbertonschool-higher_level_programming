#!/usr/bin/python3
import sys

length = len(sys.argv)
print('{} arguments:'.format(length - 1)) if length - 1 > 0 \
    else print('{} arguments.'.format(length - 1))

if length - 1 != 0:
    for i in range(1, length):
        print('{:d}: {}'.format(i, sys.argv[i]))
