#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """print x elements of a list

    Args:
        my_list: a list
        x: an integer

    Return: the real number of elements printed
    """
    elem_count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elem_count += 1
        except IndexError:
            break
    if my_list and x != 0:
        print()
    return elem_count
