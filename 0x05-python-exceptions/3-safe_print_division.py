#!/usr/bin/python3
def safe_print_division(a, b):
    """divide 2 integers and print the result

    Args:
        a: first integer
        b: second integer

    Return: the result of the division
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
