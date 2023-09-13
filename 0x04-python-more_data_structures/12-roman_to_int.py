#!/usr/bin/python3
def roman_to_int(roman_string):
    """convert a roman numeral to an integer

    Args:
        roman_string: a string

    Return: return the integer
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dic = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=100)
    result = 0
    pre = 0
    for i in range(len(roman_string)):
        post = roman_dic[roman_string[i]]
        if post > pre and i != 0:
            post = post - (pre * 2)
        pre = post
        result += pre
    return result
