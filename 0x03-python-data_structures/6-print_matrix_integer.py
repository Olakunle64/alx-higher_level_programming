#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """print matrix integer

    Args:
        matrix: nexted list

    Return: void
    """
    if not matrix:
        return
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=' ')
        print()
