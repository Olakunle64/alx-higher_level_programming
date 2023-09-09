#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replace an element in a list

    Args:
        my_list: a list
        idx: index of the element to replace
        element: element to replace with

    Return: return the new list without modifying
    my_list
    """
    if my_list is None:
        return None
    new_list = my_list[:]
    if idx < 0 or idx > len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
