#!/usr/bin/python3
"""This module supplies just a single function named
    <print_square>.

    Here is the guide on how to use it:

    print_square(4)
    result:
    """


def print_square(size):
    """print a square with the character #

    Args:
        size: an integer

    Return: void.
    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            print("#" * size)
