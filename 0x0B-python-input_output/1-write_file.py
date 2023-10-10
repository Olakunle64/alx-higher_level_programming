#!/usr/bin/python3
"""This module supplies one function named <write_file>

    Here is the guide to use the function:
    write_file(filename, text)
    """


def write_file(filename="", text=""):
    """write a string to a text file

    Args:
        filename: the name of the file
        text: text to write to the file

    Return: return the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file_object:
        char_written = file_object.write(text)
        return char_written
