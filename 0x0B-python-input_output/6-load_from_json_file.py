#!/usr/bin/python3
""" defining the function to writes object to file"""
import json


def load_from_json_file(filename):
    """
    this function writes a string to a text file
    uses the json function to change obj to str
    """
    with open(filename) as f:
        return json.load(f)
