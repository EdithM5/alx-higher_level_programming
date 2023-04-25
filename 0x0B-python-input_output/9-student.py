#!/usr/bin/python3
"""defining a class that defines a student"""


class Student:
    """
    represent a student using 3 attributes
    """
    def __init__(self, first_name, last_name, age):
        """
        initialise a new student
        @first_name
        @last_name
        @age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ get a dict representation of student"""
        return self.__dict__
