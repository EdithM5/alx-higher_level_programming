#!/usr/bin/python3

"""
defining the function that prints my name is <first name><last name>
"""


def say_my_name(first_name, last_name=""):
    """
    the arguments first name and last name must be strings
    otherwise raise: TypeError
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
