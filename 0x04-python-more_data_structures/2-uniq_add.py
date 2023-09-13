#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers

    Args:
        my_list: a list

    Return: return the result
    """
    unique_set = set(my_list)
    return sum(unique_set)
