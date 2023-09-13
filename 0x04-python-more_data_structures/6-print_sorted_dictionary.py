#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """print a dictionary by ordered keys

    Args:
        a_dictionary: a dictionary

    Return: void
    """
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))

a_dictionary = {}
print_sorted_dictionary(a_dictionary)

