#!/usr/bin/python3
""" Module 8-class_to_json.py """


def class_to_json(obj):
    """ Return:
            dictionary description with simple data structure
            for JSON serialization of an object
    """
    return obj.__dict__
