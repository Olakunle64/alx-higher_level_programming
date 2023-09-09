#!/usr/bin/python3
def max_integer(my_list=[]):
    """get the maximum integer

    Args:
        my_list: a list

    Return: return the maximum integer
    """
    if not my_list:
        return None
    _max = my_list[0]
    for num in my_list:
        if num > _max:
            _max = num
    return _max
