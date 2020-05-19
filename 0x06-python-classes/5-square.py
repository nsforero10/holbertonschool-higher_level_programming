#!/usr/bin/python3
"""Square Class"""


class Square:
    """Empty Square class"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print('#', end='')
            print()

    def area(self):
        return self.__size ** 2
