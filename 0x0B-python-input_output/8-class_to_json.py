#!/usr/bin/python3
"""function that returns a dictionary description"""


def class_to_json(obj):
    """
    Return the dictionary representation of a simple
    data structure
    obj is a class instance
    """
    return obj.__dict__
