#!/usr/bin/python3


def max_integer(list=[]):
    """Function that find and return the max integer in a list of integers
        If list is empty,function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
