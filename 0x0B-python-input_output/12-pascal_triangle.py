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
    pascal_tr = []
    if n <= 0:
        return pascal_tr
    if n >= 1:
        pascal_tr.append([1])
    if n >= 2:
        pascal_tr.append([1, 1])
    temp = 1
    while temp <= n - 2 and n > 2:
        sub_pascal = []
        i = 0
        while i < len(pascal_tr[temp]):
            result = pascal_tr[temp][i] + pascal_tr[temp][i + 1]
            sub_pascal.append(result)
            i += 1
            if i + 1 == len(pascal_tr[temp]):
                break
        sub_pascal.insert(0, 1)
        sub_pascal.insert(len(sub_pascal), 1)
        pascal_tr.append(sub_pascal)
        temp += 1
    return pascal_tr
