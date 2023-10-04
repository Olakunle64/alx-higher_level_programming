#!/usr/bin/python3
"""This module supplies one function named
    <lazy_matrix_mul>

    It takes two matrices as an argument
    """

import numpy


def lazy_matrix_mul(m_a, m_b):
    """multipy two matrices

    Args:
        m_a: matrix
        m_b: matrix

    Return: the a new list containing the
    multiplication of the two matrices
    """
    matrix_a = numpy.array(m_a)
    matrix_b = numpy.array(m_b)
    result = numpy.dot(matrix_a, matrix_b)
    return result
