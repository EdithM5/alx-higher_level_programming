#!/usr/bin/python3
""" defining a class that will inherit from list"""


class MyList(list):
    """defining a fuction that prints a sorted int list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        """prints sorted list"""
        print(sorted_list)
