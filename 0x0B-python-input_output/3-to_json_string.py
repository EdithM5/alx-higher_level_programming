#!/usr/bin/python3
"""function that returns a JSON representation(string)"""
import json


def to_json_string(my_obj):
    """
    the function will return my_obj
    as a string
    like JSON would
    """
    return json.dumps(my_obj)
