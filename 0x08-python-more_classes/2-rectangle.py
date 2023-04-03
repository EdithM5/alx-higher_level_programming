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

        def area(self):
            """calculate the area"""
            return (self._width * self._height)

        def perimeter(self):
            """calculate the perimeter"""
            if self._width == 0 or self._height == 0:
                return (0)
            else:
                return ((self._width * 2) + (self._height * 2))
