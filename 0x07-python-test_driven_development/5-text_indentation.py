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
    cpy_text = text.strip()
    puntuation = [".", ":", "?"]
    while i < len(cpy_text):
        if cpy_text[i] not in puntuation:
            print(cpy_text[i], end='')
            i += 1
            continue
        else:
            print(cpy_text[i], end='')
            print('\n')
            i += 1
            while i < len(cpy_text) and cpy_text[i] == ' ':
                i += 1
            if i < len(cpy_text) and cpy_text[i] == ' ':
                i += 1
