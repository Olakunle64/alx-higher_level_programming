#!/usr/bin/python3
"""This module contains a class named <MyInit>

    It has two methods
    """


class MyInt(int):
    """A class with two methods namely:
    __ne__ and __eq__
    """

    def __eq__(self, other):
        """work like __ne__"""
        if isinstance(other, MyInt) or issubclass(type(other), int):
            return super().__ne__(other)
        return NotImplemented

    def __ne__(self, other):
        """work like __eq__"""
        if isinstance(other, MyInt) or issubclass(type(other), int):
            return super().__eq__(other)
        return NotImplemented
