#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """square a matrix element

    Args:
        matrix: a 2D array

    Return: return a new matrix
    """
    if matrix == []:
        return None
    new_matrix = [list(map(lambda x: x ** 2, row)) for row in matrix]
    return new_matrix
