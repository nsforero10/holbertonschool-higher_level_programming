#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == '__main__':

    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    elif argv[2] not in '+-*/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        switcher = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div,
        }
        print('{} {} {} = {}'
              .format(a, argv[2], b, switcher.get(argv[2])(a, b)))
