#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """print x elements of a list and only integers

    Args:
        my_list: a list
        x: an integer

    Return: the real number of integers printed
    """
    elem_count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            elem_count += 1
        except (ValueError, TypeError):
            pass
    print()
    return elem_count
