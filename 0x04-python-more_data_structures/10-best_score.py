#!/usr/bin/python3
def best_score(a_dictionary):
    """Find the key with the biggest value

    Args:
        a_dictionary: a dictionary

    Return: the key with the biggest value
    """
    if a_dictionary == None:
        return None
    _max = max(a_dictionary.values())
    for key in a_dictionary.keys():
        if a_dictionary[key] == _max:
            return key
