#!/usr/bin/python3
"""This module supplies one funcion named <pascal_triangle>

    Here is the guide to use it:
    pascal_triangle(n)
    """


def pascal_triangle(n):
    """return a list of list of integrs representing the
    pascal's triangle of n

    Args:
        n: an integer
    """
    big_list = []
    if n <= 0:
        return big_list
    if n >= 1:
        big_list = [[1]]
    if n >= 2:
        big_list.append([1, 1])
    i = 2
    j = 0
    while n > 2:
        new_list = []
        new_list.append(1)
        while j < len(big_list[i]):
            if len(new_list) < len(big_list[i]):
                new_list.append(big_list[i][j] + big_list[i][j + 1])
            j += 1
        new_list.append(1)
        j = 0
        big_list.append(new_list)
        n -= 1
        i += 1
    return big_list
