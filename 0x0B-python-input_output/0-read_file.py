#!/usr/bin/python3
"""This module supplies one function named <read_file>

    Here is the guide to use the function:
    read_file(file_name)
    """


def read_file(filename=""):
    """read a text file and print it to stdout"""
    if not filename or filename is None:
        return
    with open(filename, "r", encoding="utf-8") as file_object:
        text_read = file_object.read()
        text_to_print = text_read[:len(text_read) - 1]
        print(text_to_print)
