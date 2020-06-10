#!/usr/bin/python3
"""
base.py
"""
import json
import csv


class Base():
    """
    Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return '[]'
    @classmethod
    def save_to_file(cls, list_objs):
        """Save into a file"""
        file = cls.__name__ + '.json'
        with open(file, 'w') as json_file:
            if list_objs is None:
                json_file.write('[]')
            else:
                dic = [obj.to_dictionary() for obj in list_objs]
                json_file.write(Base.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        """JSON to dictionary"""
        if not json_string or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a instances with set attributes"""
        if cls.__name__ == 'Rectangle':
            n = cls(1, 1)
        else:
            n = cls(1)
        n.update(**dictionary)
        return n

    @classmethod
    def load_from_file(cls):
        """loads a instances from a file"""
        try:
            with open(cls.__name__ + '.json', 'r') as f:
                jstr = f.read()
                list_d = Base.from_json_string(jstr)
                list_o = []
                for item in list_d:
                    list_o.append(cls.create(**item))
                return list_o
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves into a csv"""
        fname = cls.__name__ + ".csv"
        with open(fname, 'w', newline='') as f:
            if list_objs is None or list_objs == []:
                f.write("[]")

            else:
                if cls.__name__ == 'Rectangle':
                    h = ['id', 'width', 'height', 'x', 'y']
                else:
                    h = ['id', 'size', 'x', 'y']
                ncsv = csv.DictWriter(f, fieldnames=h)
                for obj in list_objs:
                    ncsv.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Load csv data """
        fname = cls.__name__ + '.csv'
        try:
            with open(fname, 'r', encoding='utf-8') as f:
                if cls.__name__ == 'Rectangle':
                    h = ['id', 'width', 'height', 'x', 'y']
                else:
                    h = ['id', 'size', 'x', 'y']

                csv_dict = csv.DictReader(f, fieldnames=h)
                list_dict = []
                for row in csv_dict:
                    new_dict = {}
                    for k, v in row.items():
                        new_dict[k] = int(v)
                    list_dict.append(new_dict)
                result = []
                for obj in list_dict:
                    result.append(cls.create(**obj))
                return result
        except IOError:
            return []
