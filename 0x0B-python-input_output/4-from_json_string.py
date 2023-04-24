#!/usr/bin/python3
"""function that returns an object representation from JSON"""
import json


def from_json_string(my_str):
    """
    the function will return my_str
    as an object of any kind that had been
    converted by JSON
    """
    return json.loads(my_str)
