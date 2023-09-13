#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers

    Args:
        my_list: a list

    Return: return the result
    """
    if my_list == []:
        return None
    empty_set = set()
    for num in my_list:
        empty_set.add(num)
    return sum(empty_set)
