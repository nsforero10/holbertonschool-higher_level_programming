#!/usr/bin/python3
import sys

length = len(sys.argv)

suma = 0
for i in range(1, length):
    suma += int(sys.argv[i])
print(suma)
