#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """delete an element at an index

    Args:
        my_list: a list
        idx: index of the element

    Return: return the new list or the original list if
    idx is less than 0 or is out of range
    """
    if my_list is None:
        return None
    if idx < 0 or idx > len(my_list):
        return my_list
    my_list.remove(idx + 1)
    return my_list
