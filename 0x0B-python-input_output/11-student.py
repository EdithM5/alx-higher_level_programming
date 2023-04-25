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

    def to_json(self, attrs=None):
        """
        get a dict representation of student
        If attrs is a list of strings,
        only attribute names contained in this list
        must be retrieved
        Otherwise, all attributes must be retrieved
        """
        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        function replaces all attributes of the student instance
        @json is a dictionary
        """
        for k, v in json.items():
            setattr(self, k, v)
