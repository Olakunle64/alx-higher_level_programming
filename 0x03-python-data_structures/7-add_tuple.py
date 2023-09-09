#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """add 2 tuples

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Return: return a tuple with 2 integer
    """
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    f_elem = a1 + b1
    s_elem = a2 + b2

    return (f_elem, s_elem)
