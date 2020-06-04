#!/usr/bin/python3
"""
9-add_item.py
"""
from sys import argv
save_json = __import__('7-load_to_json_file').load_from_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

try:
    i = load_json('add_item.json')
except FileNotFoundError:
    i = []
i.extend(argv[1:])
save_json(i, 'add_item.json')
