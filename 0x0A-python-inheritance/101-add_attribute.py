#!/usr/bin/python3
"""Adds an attribute to an object if possible"""


def add_attribute(obj, attr, value):
    """
    will try to add attribute

    raise Type error if it can't add attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
