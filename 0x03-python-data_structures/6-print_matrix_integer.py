#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """print matrix integer

    Args:
        matrix: nexted list

    Return: void
    """
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=' ')
        print()
