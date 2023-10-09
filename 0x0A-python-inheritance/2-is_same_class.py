#!/usr/bin/python3
"""This module supplies a function named <is_same_class>

    Here is the guide to use the function:
    is_same_class(obj, a_class)
    """


def is_same_class(obj, a_class):
    """return True if the object is exaclty an
    instance of the specifid class otherwise False

    Args:
        obj: an object
        a_class: a class
    """
    if isinstance(obj, a_class) and issubclass(a_class, type(obj)):
        return True
    else:
        return False
