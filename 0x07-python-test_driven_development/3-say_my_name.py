#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """Print a name.

    Raises:
        TypeError: If either of first_name or last_name is not a string.
    """
    if not all(isinstance(name, str) for name in [first_name, last_name]):
        raise TypeError("Both first_name and last_name must be strings")
    print(f"My name is {first_name} {last_name}")
