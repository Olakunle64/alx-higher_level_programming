#!/usr/bin/python3
"""This module supplies a function named <save_to_json_file>

    Here is the guide to use the function:
    save_to_json_file(my_obj, filename)
    """
import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file using JSON
    representation
    """
    with open(filename, "w", encoding="utf-8") as file_object:
        file_object.write(json.dumps(my_obj))
