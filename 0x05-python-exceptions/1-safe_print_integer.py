#!/usr/bin/python3
def safe_print_integer(value):
    """print an integer with str.format

    Args:
        value: an integer

    Return: True if value has been correctly
    printed or false otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
