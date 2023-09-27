#!/usr/bin/python3
"""This file contains two classes

    Aim: to implement the singly linked list
    """


class Node:
    """The class is just like a node that has a
    data and a pointer to the nextnode

    Attributes:
        data: field private attribute
        next_node: field private attribute
    """
    def __init__(self, data, next_node=None):
        """Initializing the field attribute"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """defining a getter for the data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """defining a setter for the data attribute"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """defining a getter for the next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """defining a setter for the next_node attribute"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class is meant to insert a node in a list and also
    define what would happen when the class is called with a print
    function

    Attributes:
        __str__: method to define what will happen when the class is
        called in a print function
        sorted_insert: method to insert the newnode
    """
    def __init__(self):
        """Initializing the pointer to the first node as a private field
        with no getter and setter
        """
        self.__head = None

    def sorted_insert(self, value):
        """inserting a newnode of class Node"""
        newnode = Node(value)
        if self.__head is None or value < self.__head.data:
            newnode.next_node = self.__head
            self.__head = newnode
        else:
            current = self.__head
            while (current.next_node is not None and
            current.next_node.data < value):
                current = current.next_node
            newnode.next_node = current.next_node
            current.next_node = newnode

    def __str__(self):
        """defining what will happend when the class is called with the print
        function
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
