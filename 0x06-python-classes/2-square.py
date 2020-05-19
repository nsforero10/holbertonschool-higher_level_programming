#!/usr/bin/python3
"""Square Class"""


class Square:
    """Empty Square class"""
    def __init__(self, size=0):
        if type(size) != int:
            TypeError('size must be a integer')
        if size < 0:
            raise ValueError('size must be >=0')
        self.__size = size
