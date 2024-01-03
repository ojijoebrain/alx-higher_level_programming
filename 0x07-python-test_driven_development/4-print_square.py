#!/usr/bin/python3


def print_square(size):
    """Print a square with the # character.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for j in range(size):
        [print("#", end="") for i in range(size)]
        print("")
