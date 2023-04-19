#!/usr/bin/python3
"""
the class is designed
"""


class MyInt(int):
    """
    A class that inverts int operators == and !=.
    """

    def __eq__(self, value):
        """
        overide == to !=.
        """
        return (self.real != value)

    def __ne__(self, value):
        """
        overide != to ==
        """
        return (self.__real == value)
