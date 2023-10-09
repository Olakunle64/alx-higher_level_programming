#!/usr/bin/python3
"""This module contains a class named <Rectangle> that inherits
    from <BaseGeometry>
    """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class has only one method with two field
    attributes

    Methods: __init__
    Args:
        width: an integer
        height: an integer
    """
    def __init__(self, width, height):
        """initializing and validating arguments"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string implementation"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
