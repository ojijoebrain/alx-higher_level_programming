#!/usr/bin/python3
""" Module 9-student.py """


class Student():
    """ class defines student by some parameters """

    def __init__(self, first_name, last_name, age):
        """ initialises  attributs of the Student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrives a dictionary representation of a Student instatnce """
        return self.__dict__
