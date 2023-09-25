#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """print an integer

    Args:
        value: an integer

    Return: True if value has been correctly printed
    or false otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return False
