#!/usr/bin/python3
"""This module contains a class named LockedClass

    It has no method or attribute
    """


class LockedClass:
    """Empty class with instance attribute locked"""

    def __setattr__(self, name, value):
        """set a constant attribute"""
        if name != "first_name":
            raise AttributeError(
            "'LockedClass' object has no attribute '{}'".format(name)
            )
