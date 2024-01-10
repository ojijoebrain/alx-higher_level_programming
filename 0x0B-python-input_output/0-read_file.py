#!/usr/bin/python3
""" Module 0-read_file.py """


def read_file(filename=""):
    """ reads a text file and prints it's content """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
