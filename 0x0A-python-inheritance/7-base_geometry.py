#!/usr/bin/python3
"""This module contains a class named <BaseGeometry>

    It is an empty class
    """


class BaseGeometry:
    """This class has no attribute"""

    def area(self):
        """raise an exception that area is not defined"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate if value is an integer"""
        if type(name) is not str:
            raise Exception
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
