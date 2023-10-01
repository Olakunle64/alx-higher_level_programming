#!/usr/bin/python3
"""This module supplies just a single function named
    <text_indentation>

    Here is the guide on how to use it:

    text_indentation("I am a graduate")
    result: I am a graduate
    """
def text_indentation(text):
    """print a text with 2 newlines after each of these
        characters: . ? :

    Args:
        text: a string

    Return: void
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not text:
        print()
    i = 0
    while i < len(text):
        if text[i] == '.' or text[i] == ':' or text[i] == '?':
            print(text[i], end='')
            print('\n')
            if i + 1 < len(text) and text[i + 1] == ' ':
                    i = i + 2
            else:
                i = i + 1
            continue
        print(text[i], end='')
        i = i + 1
