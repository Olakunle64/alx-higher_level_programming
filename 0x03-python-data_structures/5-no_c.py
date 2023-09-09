#!/usr/bin/python3
def no_c(my_string):
    """removes characters

    Args:
        my_string: a string

    Return: return the new string
    """
    new_string = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_string += ch
    return new_string
