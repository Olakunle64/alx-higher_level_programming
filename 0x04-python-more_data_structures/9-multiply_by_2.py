#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Multiply all values of a dictionary by 2

    Args:
        a_dictionary: a dictionary

    Return: return a new dictionary
    """
    new_dic = {}
    for key in a_dictionary.keys():
        new_dic[key] = a_dictionary[key] * 2
    return new_dic
