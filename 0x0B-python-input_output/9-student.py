#!/usr/bin/python3
"""This module contains a class named <Student>

    It has 3 public field attributes and a method
    """


class Student:
    """This class has the following attribute
    Field: first_name, last_name and age
    Method: __init__ and to_json
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return the dictionary description of an object"""
        if hasattr(self, "__dict__"):
            obj_dict = self.__dict__.copy()
            for key in obj_dict:
                if isinstance(key, (list, int, dict, bool, str)):
                    continue
                else:
                    obj_dict[key] = str(obj_dict[key])
            return obj_dict
        else:
            return self.__str__()
