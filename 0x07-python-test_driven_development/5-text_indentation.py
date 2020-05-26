#!/usr/bin/python3
"""
    Text indentation file
"""


def text_indentation(text):
    """
        prints a text with 2 new lines after each of these characters: ., ? and :
    """

    breakers = ['.', '?', ':']
    if type(text) is not str:
        raise TypeError('text must be a string')
    for c in range(len(text)):
        if text[c] == ' ' and text[c - 1] in breakers:
            continue
        print(text[c], end='')
        if text[c] == '.' or text[c] == '?' or text[c] == ':':
            print('', end='\n\n')
