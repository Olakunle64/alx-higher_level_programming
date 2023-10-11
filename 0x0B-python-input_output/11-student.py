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
        """initialization of attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return the dictionary description of an object"""
        if hasattr(self, "__dict__") and isinstance(attrs, list):
            obj_dict = self.__dict__.copy()
            new_list = []
            for key in obj_dict:
                if key in attrs:
                    continue
                else:
                    new_list.append(key)
            for value in new_list:
                del obj_dict[value]
            return obj_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replace all attribute of an instance"""
        if hasattr(self, "__dict__") and isinstance(json, dict):
            for key, value in json.items():
                setattr(self, key, value)

