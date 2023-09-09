#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """replace in list

    Args:
        my_list: a list
        idx: index of the element to replace
        element: element to replace with

    Return: return the new list or old list if idx is
            negative or out of range
    """
    if my_list is None:
        return my_list
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
