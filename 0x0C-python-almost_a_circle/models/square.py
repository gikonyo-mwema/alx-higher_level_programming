#!/usr/bin/python3
"""
This module defines the Square class which inherits from the Rectangle class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class to represent a square.

    ...

    Attributes
    ----------
    size : int
        size of the square
    x : int
        x-coordinate of the square
    y : int
        y-coordinate of the square
    id : int
        unique id for the square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructs all the necessary attributes for the Square object.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates attributes of the square.
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
        """
        Returns the dictionary representation of a Square instance.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Returns the string representation of a Square instance.
        """
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.width))
