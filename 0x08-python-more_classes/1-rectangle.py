#!/usr/bin/python3

"""Defining a Rectangle"""


class Rectangle:

    """Adding rectangle objects"""

    def __init__(self, width=0, height=0):
        """Initialialize a new Rectangle.

        private attributes:
        width: which is the width
        height: which is the height
        """
        self._width = width
        self._height = height

        @property
        def width(self):
            """set the width"""
            return self._width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self._width = value

        @property
        def height(self):
            """set the height"""
            return self._height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >=0")
            self._height = value
