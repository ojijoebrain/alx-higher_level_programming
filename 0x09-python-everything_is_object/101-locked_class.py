#!/usr/bin/python3
"""To defines locked class."""


class LockedClass:
    """
    To stop user from instantiating new LockedClass attributes
    in anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
