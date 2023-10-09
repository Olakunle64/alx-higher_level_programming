#!/usr/bin/python3
"""This module supplies a function named <lookup>

    Here is the guide to use it:
    lookup(obj)
    """


def lookup(obj):
    """return the list of available attritutes and
    methods of an object

    Args:
        obj: an object

    Return: return a list
    """
    return dir(obj)
