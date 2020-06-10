#!/usr/bin/python3
"""
square.py
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.height)

    @property
    def size(self):
        """size getter"""
        return self.height

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Update square class """
        if len(args):
            key = ['id', 'size', 'x', 'y']
            for i in range(0, len(args)):
                if i < 4:
                    setattr(self, key[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
