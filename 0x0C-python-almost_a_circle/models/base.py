#!/usr/bin/python3
"""This module contains a class named <Base>
    It has one special method(__init__)

    It also has a private class attribute
    """


class Base:
    """Base class

    methods: __init__
    fields:
        class field: __nb_objects
        instance field: id
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """initializing instance attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
