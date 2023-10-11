#!/usr/bin/python3
"""This module contains a function named <class_to_json>

    Here is the guide to use the function:
    class_to_json(obj)
    """


def class_to_json(obj):
    """return the dictionary description with simple
    data structure
    """
    if hasattr(obj, "__dict__"):
        obj_dict = obj.__dict__.copy()
        for key in obj_dict:
            if isinstance(key, (list, bool, str, int, dict)):
                continue
            else:
                obj_dict[key] = str(obj_dict[key])
        return obj_dict
    else:
        return obj_dict.__str__()
