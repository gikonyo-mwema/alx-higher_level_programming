#!/usr/bin/python3
"""
This is the "base" module.

The base module supplies one class, Base. For example,

>>> b = Base(1)
>>> b.id
1
"""


class Base:
    """Base model.

    This represents the 'base' for all other classes.

    Private Class Attributes:
        _nb_objects (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
