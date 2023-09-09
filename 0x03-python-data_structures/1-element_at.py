#!/usr/bin/python3

def element_at(my_list, idx):
    """element at

    Args:
        my_list: a list
        idx: the index of the element

    Return: return the element at idx
    """
    if idx < 0 or idx > len(my_list):
        return None
    for flag, ch in enumerate(my_list):
        if idx == flag:
            return ch
