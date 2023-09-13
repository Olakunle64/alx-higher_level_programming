#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another

    Args:
        my_list: a list
        search: element to search
        replace: element to replace

    Return: return the new list
    """
    if my_list == None:
        return None
    new_list = my_list[:]
    for i in range(len(new_list)):
        new_list[i] = replace if new_list[i] == search else new_list[i]
    return new_list
