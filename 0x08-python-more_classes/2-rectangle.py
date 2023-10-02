#!/usr/bin/python3
"""This module contains a class named <Rectangle>

    <Rectangle> has two instance variable with their
    respective getters and setters(@property)

    Methods: area() and perimeter()
    """


class Rectangle:
    """A class called <Rectangle>

    instance variable: width and height(with
    respective getters and setters)

    Methods:
        area(): to get the area of the rectangle
        perimeter(): to get the perimeter of the rectangle
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

    def area(self):
        """return the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of a rectangle"""
        if not self.__width or not self.__height:
            return 0
        return 2 * (self.__width + self.__height)
