#!/usr/bin/python
def magic_calculation(a, b):
    """write a python function that suit a particular
    bytecode

    Args:
        a: integer
        b: integer

    Return: void
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
        except Exception:
            result = a + b
            break
    return result
