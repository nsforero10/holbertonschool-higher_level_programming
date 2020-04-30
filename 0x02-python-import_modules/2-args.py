#!/usr/bin/python3
import sys
if __name__ == '__main__':

    length = len(sys.argv) - 1
    print('{} arguments:'.format(length)) if length > 1 \
        else print('{} arguments.'.format(length))

    if length != 0:
        for i in range(1, length + 1):
            print('{:d}: {}'.format(i, sys.argv[i]))
