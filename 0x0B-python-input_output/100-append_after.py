#!/usr/bin/python3
"""This module supplies a function named <append_after>

    Here is the guide to use the function:
    append_after(filename="", search_string="", new_string="")
    """


def append_after(filename="", search_string="", new_string=""):
    """insert a line of text to a file after each line
    containing a specific string
    """
    file_text = []
    with open(filename, "r", encoding="utf-8") as file_obj:
        for line in file_obj:
            file_text.append(line)
            if search_string in line:
                file_text.append(new_string)
    with open(filename, "w", encoding="utf-8") as file_obj:
        for line in file_text:
            file_obj.write(line)
