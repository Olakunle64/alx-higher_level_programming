#!/usr/bin/python3
"""This module contains a class named <Square> which
    inherit from <Rectangle>
    """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class has only one method

    Methods: __init__ and area()

    Field: size
    """
    def __init__(self, size):
        """initialize the self attribute"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """string implemtation"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
