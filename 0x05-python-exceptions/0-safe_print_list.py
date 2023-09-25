#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """print x elements of a list

    Args:
        my_list: a list
        x: an integer

    Return: the real number of elements printed
    """
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            if i == x - 1:
                print()
                return i + 1
        except IndexError:
            print()
            return i
