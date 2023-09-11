#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """print matrix integer

    Args:
        matrix: nexted list

    Return: void
    """
    if not matrix:
        print()
    else:
        for row in matrix:
            i = 0
            if not row:
                continue
            for col in row:
                i += 1
                print("{:d}".format(col), end=' ' if i != len(row) else '\n')
