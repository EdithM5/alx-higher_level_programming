#!/usr/bin/python3
""" defining the function to append file"""


def append_write(filename="", text=""):
    """
    this function appends a string to a text file
    and prints out the number of characters appended
    txt is the text to append
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
