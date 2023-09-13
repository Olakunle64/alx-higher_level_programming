#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """delete keys with specific value in a dic

    Args:
        a_dictionary: a dictionary
        value: the specific value

    Return: new dictionary
    """
    if a_dictionary is None:
        return None
    list_to_delete = []
    for key in a_dictionary.keys():
        if a_dictionary[key] == value:
            list_to_delete.append(key)
    for ch in list_to_delete:
        del a_dictionary[ch]
    return a_dictionary
