#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """delete a key in a dictionary

    Args:
        a_dictionary: a dictionary
        key: name of the key to delete

    Return: the new dictionary
    """
    if key == "":
        return a_dictionary
    if a_dictionary.get(key, 2) != 2:
        del a_dictionary[key]
    return a_dictionary
