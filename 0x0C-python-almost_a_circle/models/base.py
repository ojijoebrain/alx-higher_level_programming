#!/usr/bin/python3
""" The base model """


class Base():
    """ The Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ It initializes the id attribute """
        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_object
