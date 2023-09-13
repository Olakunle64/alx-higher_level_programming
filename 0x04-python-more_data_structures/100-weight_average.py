#!/usr/bin/python3
def weight_average(my_list=[]):
    """find the weighted average of all integers tuple

    Args:
        my_list: a list

    Return: 0 if the list is empty or the weighted average
    """
    if my_list == []:
        return 0
    new_list = list(map(lambda x: (x[0] * x[1]), my_list))
    Total_weight = list(map(lambda x: x[1], my_list))
    return (sum(new_list) / sum(Total_weight))
