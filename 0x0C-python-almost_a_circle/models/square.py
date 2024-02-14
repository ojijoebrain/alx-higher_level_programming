#!/usr/bin/python3
"""This is square model."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square representation."""

    def __init__(self, size, x=0, y=0, id=None):
        """New Square Initialization.

        Parameters:
            size (int): Size of the new Square.
            x (int): Coordinate x of the new Square.
            y (int): Coordinate y of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Set size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Square Update.

        Parameters:
            *args (ints): Value New attribute.
                - 1st argument represents attribute id
                - 2nd argument represents attribute size
                - 3rd argument represents attribute x
                - 4th argument represents attribute y
            **kwargs (dict): The new value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ Dictionary representation of the Square should be return."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """The print() and str() representation of Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
