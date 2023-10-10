#!/usr/bin/python3
"""This module supplies a function named <append_write>

    Here is the guide to use the function:
    append_write(filename, text)
    """


def append_write(filename="", text=""):
    """append a string at the end of a text file

    Args:
        filename: the file name
        text: text to append to filename

    Return: return the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file_object:
        char_appended = file_object.write(text)
        return char_appended
