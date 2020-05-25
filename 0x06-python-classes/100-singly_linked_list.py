#!/usr/bin/python3
"""Node class"""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

    def __str__(self):
        return str(self.__data)


class SinglyLinkedList:
    """Empty SinglyLinkedList class"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        tmp = self.__head
        while (tmp.next_node is not None):
                 if (tmp.next_node.next_node is not None and
                        tmp.next_node.next_node.data > value):
                     break
            tmp = tmp.next_node
        new.next_node = tmp.next_node.next_node
        tmp.next_node = new
