#!/usr/bin/python3
""" 
defining a class that will inherit from list
"""


class MyList(list):
    """defining a fuction that prints a sorted int list"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
