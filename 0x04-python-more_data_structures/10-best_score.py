#!/usr/bin/python3
def best_score(a_dictionary):
    """Find the key with the biggest value

    Args:
        a_dictionary: a dictionary

    Return: the key with the biggest value
    """
    if a_dictionary is None:
        return None
    _max = 0
    for key, value in a_dictionary.items():
        if value > _max:
            max_key = key
        _max = value
    return max_key
