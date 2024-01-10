#!/usr/bin/python3
""" Module 6-load_from_json_file.py """


import json


def load_from_json_file(filename):
    """ create an object from JSON file """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
