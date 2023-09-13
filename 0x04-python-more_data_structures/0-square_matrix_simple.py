#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """square a matrix element

    Args:
        matrix: a 2D array

    Return: return a new matrix
    """
    if matrix == []:
        return None
    new_matrix = [[col ** 2 for col in row] for row in matrix if row]
    return new_matrix
