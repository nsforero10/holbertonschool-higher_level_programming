#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        Unit test for maxint
    """
    def average_case(self):
        lis = [1, 2, 3, 4, 5]
        self.assertEquals(max_integer(lis), 5)

    def none_case(self):
        lis = []
        self.assertEquals(max_integer(lis), None)

    def string_case(self):
        lis = ['hello world']
        self.assertEquals(max_integer(lis), 'h')

    def different_types_case(self):
        lis = ['1', 2, 3.4]
        with self.assertRaises(TypeError):
            max_integer(lis)

    def lessthanzero_case(self):
        lis = [-1, -2, -3, -4, -5]
        self.assertEquals(max_integer(lis), -1)


if __name__ == '__main__':
    unittest.main()
