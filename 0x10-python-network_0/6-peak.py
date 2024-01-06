#!/usr/bin/python3
"""This module contains a function that check for the peak
    in a list of integer
    """


def find_peak(list_of_integers):
    """find the peak among the list of integers

        Args:
            list_of_integers: list of integers

        Return: the peak
    """
    if not list_of_integers or len(list_of_integers) < 1:
        return None
    length = len(list_of_integers)
    i = 0
    while i < length:
        if i == 0:
            maxi = list_of_integers[i]
        if list_of_integers[i] >= maxi:
            maxi = list_of_integers[i]
        elif i + 1 < length:
            if maxi > list_of_integers[i + 1]:
                return maxi
        i += 1
    return maxi
