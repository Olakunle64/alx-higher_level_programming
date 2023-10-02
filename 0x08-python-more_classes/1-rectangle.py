#!/usr/bin/python3
"""This module contains a class named <Rectangle>

    <Rectangle> has two instance variable with their
    respective getters and setters(@property)
    """


class Rectangle:
    """A class called <Rectangle>

    instance variable: width and height(with
    respective getters and setters)
    """
    def __init__(self, width=0, height=0):
        """initialization of the two instance variables"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """a getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """a setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """a getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """a setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
