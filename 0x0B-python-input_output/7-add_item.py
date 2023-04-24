#!/usr/bin/python3
""" defining the function that adds to a pythos list and saves"""
import sys
from os import path


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"

    if not path.exists(filename):
        items = []
    else:
        items = load_from_json_file(filename)

    for arg in sys.argv[1:]:
        items.append(arg)

    save_to_json_file(items, filename)
