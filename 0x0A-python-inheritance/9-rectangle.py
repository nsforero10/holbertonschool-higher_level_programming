#!/usr/bin/python3
"""
9-rectangle.py
"""
BaseGeometry = __import__('7-base-geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from base geometry"""
    def __init(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ calculates the area"""
        return self.__width * self.__height

    def __str__(self):
        """str representation"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
