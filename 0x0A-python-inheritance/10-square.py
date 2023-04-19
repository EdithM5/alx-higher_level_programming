#!/usr/bin/python3
"""
the class is designed
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.
    """
    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the Square.

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
