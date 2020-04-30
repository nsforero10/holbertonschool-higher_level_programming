#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == '__main__':

    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    elif argv[2] not in '+-*/':
        print("Unknown operator. Available operators: +, -, * and /")
    else:
        a = int(argv[1])
        b = int(argv[3])
        switcher = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div,
        }
        print(switcher.get(argv[2])(a, b))
