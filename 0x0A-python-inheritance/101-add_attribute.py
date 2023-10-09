#!/usr/bin/python3
"""This module supplies a function named <add_attribute>

    it takes 3 arguments
    """


def add_attribute(obj, att_name, att_value):
    """add a new attribute to an object if it's possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, att_name, att_value)
    else:
        raise TypeError("can't add new attribute")
