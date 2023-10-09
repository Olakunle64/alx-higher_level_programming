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
