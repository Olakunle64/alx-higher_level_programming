#!/usr/bin/python3
"""This module supplies just a single function named
    <say_my_name>

    Here is the guide on how to use it:

    say_my_name("salau", "isiaq")
    result: My name is salau isiaq
    """


def say_my_name(first_name, last_name=""):
    """say my name function

    Args:
        first_name: a string
        last_name: a string

    Return: void
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if not first_name and not last_name:
        print("My name is")
    elif not first_name:
        print("My name is {}".format(last_name))
    elif not last_name:
        print("My name is {}".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
