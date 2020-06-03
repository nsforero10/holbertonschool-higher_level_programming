#!/usr/bin/python3
"""
11-square.py
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from rectangle """
    def __init__(self, size):
        """ Constructs a square """
        if self.integer_validator("size", size):
            self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ str representation """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
