#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """check for number divisible by 2

    Args:
        my_list: a list

    Return: a new list containing True or False
    """
    if my_list is None:
        return None
    new_list = my_list[:]
    i = 0
    for num in new_list:
        if num % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
        i += 1
    return new_list
