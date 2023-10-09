#!/usr/bin/python3
"""This module supplies a function named <is_kind_of_class>

    Here is the guide to use the function:
    is_kind_of_class(obj, a_class)
    """


def is_kind_of_class(obj, a_class):
    """return True if the object is an instance of or
    if the object is an instance of a class that inherited
    from the specified class otherwise return False.

    Args:
        obj: an object
        a_class: a class
    """
    if isinstance(obj, a_class) or issubclass(a_class, type(obj)):
        return True
    else:
        return False
