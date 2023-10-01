#!/usr/bin/python3
"""This module supplies just a single function named
    matrix_divided.

    Here is the guide on how to use it:

    matrix_divided([[2, 3], [4, 5]], 2)
    result:
    """
def matrix_divided(matrix, div):
    """divides all the elements of a matrix

    Args:
        matrix: a list of list of integers or floats
        div: an integer or a float

    Return: return a new matrix
    """
    new_list = []
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix, list) or not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_length = len(matrix[0])
    for row in matrix:
        sub_list = []
        if not isinstance(row, list) or row == []:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if type(div) not in [int, float]:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            result = col / div
            if isinstance(result, float):
                sub_list.append(round(result, 2))
            else:
                sub_list.append(result)
        new_list.append(sub_list)
    return new_list



        
