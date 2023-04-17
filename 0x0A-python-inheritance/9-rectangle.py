#!/usr/bin/python3
"""
the class is designed
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If the width or height is not an integer.
            ValueError: If the width or height is less than or equal to zero.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")

    def area(self):
        """
        Computes the area of the Rectangle instance.

        Returns:
            The area of the rectangle.
        """
        return (self.__width * self.__height)
