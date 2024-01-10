#!/usr/bin/python3
""" Module 10-student.py """


class Student():
    """ Student class attributes and a public method
        to retrive  dict representation of  instance
    """
    def __init__(self, first_name, last_name, age):
        """ initialise the attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrives a dict representation of an instance """
        if attrs:
            attr = {}
            for j in attrs:
                if j in self.__dict__.keys():
                    attr[j] = self.__dict__[j]
            return attr
        else:
            return self.__dict__
