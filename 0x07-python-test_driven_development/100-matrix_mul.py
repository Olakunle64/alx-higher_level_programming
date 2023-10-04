#!/usr/bin/python3
"""This module supplies just a single function named <matrix_mul>

    It takes two matrices as an argument
    """


def matrix_mul(m_a, m_b):
    """mulitpy 2 matrices

    Args:
        m_a: matrix
        m_b: matrix

    Return: the new list containing the result of the multiplication
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    m_a_row_length = len(m_a[0])
    for row in m_a:
        if len(row) != m_a_row_length:
            raise TypeError("each row of m_a must be of the same size")
    m_b_row_length = len(m_b[0])
    for row in m_b:
        if len(row) != m_b_row_length:
            raise TypeError("each row of m_b must be of the same size")
    if m_a_row_length != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new_list = []
    for row in m_a:
        continous = 0
        k = 0
        sub_list = []
        while continous < m_b_row_length:
            i = 0
            j = 0
            result = 0
            while i < len(row):
                result += row[i] * m_b[j][k]
                i += 1
                j += 1
            sub_list.append(result)
            continous += 1
            k += 1
        new_list.append(sub_list)
    return new_list
