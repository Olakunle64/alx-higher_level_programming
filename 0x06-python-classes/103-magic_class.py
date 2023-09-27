#!/usr/bin/python3
"""This file contains class called MagicClass

    It has 3 methods and one field attribute
    """


class MagicClass:
    """MagicClass

    Attributes:
        __init__: first method
        area: second method
        circumference: third method
    """

    def __init__(self, radius=0):
        """initializing radius"""
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError("radius must be a number")
            self.__radius = radius

    def area(self):
        """return the area of of the radius"""
        return (self.radius ** 2) * math.pi

    def circumference(self):
        """return the circumference of the radius"""
        return 2 * math.pi * self.radius
