#!/usr/bin/python3
""" Module 1-write_file.py """


def write_file(filename="", text=""):
    """ A  string to a text file in utf-8
        Return: number of characters writen
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
