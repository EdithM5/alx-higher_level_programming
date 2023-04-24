#!/usr/bin/python3
""" defining the function to read file"""


def write_file(filename="", text=""):
    """
    this function writes a string to a text file
    and prints out the number of characters
    txt is the text to write
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
