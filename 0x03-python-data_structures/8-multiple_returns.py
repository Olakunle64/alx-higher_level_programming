#!/usr/bin/python3
def multiple_returns(sentence):
    """multiple returns

    Args:
        sentence: a string

    Return: returns a tuple with the length of a string
    and its first character
    """
    length = len(sentence)
    return (length, sentence[0] if length > 0 else None)
