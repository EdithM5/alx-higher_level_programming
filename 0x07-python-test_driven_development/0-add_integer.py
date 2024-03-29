#!/usr/bin/python3

"""
Creating a function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    return the addition of a and b.
    float numberes should be converted to int first
    Raise TypeError: if a or b is non-integer/float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (int(a) + int(b))
