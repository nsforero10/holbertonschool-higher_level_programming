#!/usr/bin/python3
"""Square Class"""


class Square:
    """Empty Square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if (type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        if self.size != 0:
            if self.position[1] != 0:
                print('\n' * self.position[1], end='')
            for i in range(self.size):
                print(' ' * self.position[0], end='')
                print('#' * self.size)
        else:
            print()

    def area(self):
        return self.__size ** 2
