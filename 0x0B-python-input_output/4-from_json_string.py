#!/usr/bin/python3
"""This module supplies one function named <from_json_string>

    Here is the guide to use the function:
    from_json_string(my_str)
    """
import json


def from_json_string(my_str):
    """return an object represented by a JSON string"""
    return json.loads(my_str)
