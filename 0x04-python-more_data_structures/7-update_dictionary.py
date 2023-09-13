#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replace or add key/value in a dictionary

    Args:
        a_dictionary: a dictionary
        @key: new key to be added to the dictionary
        @value: new value to be added to the dictionary

    Return: return the updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
