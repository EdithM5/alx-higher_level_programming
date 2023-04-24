#!/usr/bin/python3
""" defining the function to writes object to file"""
import json


def save_to_json_file(my_obj, filename):
    """
    this function writes a string to a text file
    uses the json function to change obj to str
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
