#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

av = sys.argv
for v in av:
    print(v)
if len(av) != 4:
    print('Usage: ./100-my_calculator.py <a> <operator> <b>')
    exit(1)
elif av[2] not in '+-*/':
    print("Unknown operator. Available operators: +, -, * and /")
else:
    switcher = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div,
    }
    print(switcher.get(av[2])(int(av[1]), int(av[3])))
