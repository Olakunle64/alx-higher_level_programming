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
    for i in range(1, 4):
        try:
            if i > a:
                raise Exception('Too far')
            result = a ** b
            result /= result
        except Exception:
            result = a + b
            break
    return result
