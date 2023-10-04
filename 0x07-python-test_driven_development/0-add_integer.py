#!/usr/bin/python3
"""This module supplies just a single function named add_integer
    Here is the guide to use the function:
    add_integer(2, 3)
    5
    """


def add_integer(a, b=98):
    """return the addition of two integer
    Args: a(an integer), b(an integer), return the result
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    try:
        a = int(a)
    except ValueError as errmsg:
        raise ValueError(errmsg)
    try:
        b = int(b)
    except ValueError as errmsg:
        raise ValueError(errmsg)
    return a + b
