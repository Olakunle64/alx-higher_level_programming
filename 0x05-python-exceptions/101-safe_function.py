#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """execute a function safely

    Args:
        fct: a pointer to a function
        args: arbitrary argument

    Return: the result of the function or
    None otherwise
    """
    try:
        result = fct(*args)
        return result
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
