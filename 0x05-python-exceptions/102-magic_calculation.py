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
            result = a + b
        except:
            if i > a:
                raise Exception('Too far')
            else:
                result = a ** b
                result /= result
            break;
        finally:
            result = a + b
    return result
