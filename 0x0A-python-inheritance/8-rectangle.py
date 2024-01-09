#!/usr/bin/python3
""" Module 8-rectangle.py."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """It Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """To intialize a new Rectangle.

        Args:
            width (int): Width of the new Rectangle.
            height (int): Height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
