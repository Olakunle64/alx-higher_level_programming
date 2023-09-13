#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """find only different elements in both set

    Args:
        set_1: first set
        set_2: second set

    Return: return new set containing element set_1 and set_2
    but not in both
    """
    return (set_1 ^ set_2)
