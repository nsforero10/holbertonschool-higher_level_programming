#!/usr/bin/python3
"""
7-base_geometry.py
"""


class BaseGeometry:
    """ BaseGeometry class"""
    def area(self):
        """ area function """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer validator"""
        if not isinstance(value, int):
            raise TypeError('{} must be integer'.format(name))
        if value <= 0:
            raise TypeError('{} must be greater than 0'.format(name))
