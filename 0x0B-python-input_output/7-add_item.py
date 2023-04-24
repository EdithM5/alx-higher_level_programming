#!/usr/bin/python3
""" defining the function that adds to a pythos list and saves"""
import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


filename = "add_item.json"

if not path.exists(filename):
    items = []
else:
    items = load_from_json_file(filename)

for arg in sys.argv[1:]:
    items.append(arg)

save_to_json_file(items, filename)
