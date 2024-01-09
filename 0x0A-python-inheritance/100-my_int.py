#!/usr/bin/python3
""" This is module 100-my_int.py."""


class MyInt(int):
    """This invert int operators == and !=."""

    def __eq__(self, value):
        """This override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
