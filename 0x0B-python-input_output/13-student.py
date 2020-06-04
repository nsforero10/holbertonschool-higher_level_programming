#!/usr/bin/python3
"""
13-student.py
"""

class Student:
    """ student class"""

    def __init__(self, first_name, last_name, age):
        """ constructs a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns json representation"""
        if type(attrs) == list and all(type(item) == str for item in attrs):
            d = {}
            for i in attrs:
                if i in self.__dict__:
                    d[i] = self.__dict__[i]
            return d
        return self.__dict__

    def reload_from_json(self, json):
        """ reloads the student from a json"""
        for k, v in json.items():
            self.__dict__[k] = v
