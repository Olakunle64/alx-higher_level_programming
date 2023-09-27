#!/usr/bin/python3

import math
"""This module is imported to make use of the
    pi function in it.

    pi: is just like 22 / 7
    """

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
        else:
            self.__radius = float(radius)

    def area(self):
        """return the area of of the radius"""
        return (self.__radius ** 2) * math.pi)

    def circumference(self):
        """return the circumference of the radius"""
        return (2 * math.pi * self.__radius)
