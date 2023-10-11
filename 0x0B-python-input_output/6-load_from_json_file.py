#!/usr/bin/python3
"""This module supplies a function <load_from_json_file>

    Here is the guide to use the function:
    load_from_json_file(filename)
    """
import json


def load_from_json_file(filename):
    """create an object from JSON file"""
    with open(filename, "r", encoding="utf-8") as file_object:
        return json.load(file_object)
