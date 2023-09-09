#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list in reverse

    Args:
        my_list: a list

    Return: void
    """
    if not my_list:
        return
    for num in reversed(my_list):
        print("{:d}".format(num))
