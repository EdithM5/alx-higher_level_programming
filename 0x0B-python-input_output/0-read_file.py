#!/usr/bin/python3
""" defining the function to read file"""


def read_file(filename=""):
    """
    this function reads a text file
    and prints it to stdout
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
