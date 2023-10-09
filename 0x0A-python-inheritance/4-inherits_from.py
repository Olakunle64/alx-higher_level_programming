#!/usr/bin/python3
"""This module supplies a function named <inherits_from>

    Here is the guide to use the function:
    inherits_from(obj, a_class)
    """


def inherits_from(obj, a_class):
    """return True if the object is an instance of a class
    that inherited(directly or indirectly) from the specified
    class otherwise return False.

    Args:
        obj: an object
        a_class: a class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
