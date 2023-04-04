#!/usr/bin/python3
"""Define the class"""


class LockedClass:

    """
    prevents user from creating new attributes except
    for first name
    """
    __slots__ = ["first_name"]
