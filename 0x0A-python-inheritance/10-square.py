#!/usr/bin/python3
""" This is 10-square.py."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ It represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
