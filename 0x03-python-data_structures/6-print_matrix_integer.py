#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """print matrix integer

    Args:
        matrix: nexted list

    Return: void
    """
    i = 0
    for row in matrix:
        for col in row:
            print("{}".format(col), end=' ')
        i += 1
        print()
