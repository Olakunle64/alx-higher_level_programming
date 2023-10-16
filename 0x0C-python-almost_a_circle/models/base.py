#!/usr/bin/python3
"""This module contains a class named <Base>
    It has one special method(__init__)

    It also has a private class attribute
    """
import json
import os


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
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert list_dictionary to json string"""
        if not list_dictionaries or list_dictionaries is None:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write json representation of list_objs to a file"""
        if list_objs is None:
            with open(cls.__name__ + ".json", "w", encoding="utf-8")
            as file_obj:
                file_obj.write(Base.to_json_string([]))
        else:
            if all(type(item) is cls for item in list_objs):
                new_list = []
                for obj in list_objs:
                    new_list.append(obj.to_dictionary())
                with open(cls.__name__ + ".json", "w", encoding="utf-8")
                as file_obj:
                    file_obj.write(Base.to_json_string(new_list))
            else:
                return

    @staticmethod
    def from_json_string(json_string):
        """return the original list from the json string representation
        (json_string)
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes set"""
        dummy = cls(4, 6)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of an instances"""
        new_list = []
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return new_list
        with open(filename, "r", encoding="utf-8") as file_obj:
            loaded_list = cls.from_json_string(file_obj.read())
            for obj_dict in loaded_list:
                new_list.append(cls.create(**obj_dict))
            return new_list
