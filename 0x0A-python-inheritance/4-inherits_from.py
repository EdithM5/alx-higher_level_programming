#!/usr/bin/python3
"""
Defining the function
"""


def inherits_from(obj, a_class):
    """
    the function should return
    True if object isinstance
    false if not
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
