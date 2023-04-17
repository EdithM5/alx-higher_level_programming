#!/usr/bin/python3
"""
defining the class
"""


class BaseGeometry:
    """
    the class is defined to represent
    """
    def area(self):
        """
        the area is yet to implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        it should validate value
        name is always a string
        if value != int raise TypeError
        if value <= 0 raise Value error
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
