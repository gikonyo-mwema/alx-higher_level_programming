#!/usr/bin/python3
"""A module for a square"""


class Square:
    """
    This class represents a square.
    It has a private instance attribute: size.
    """
    def __init__(self, size=0):
        """
        Initializes the square.
        Args:
            size (int, optional): The size of the square. Defaults to 0.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Return the current square area.
        """
        return self.__size ** 2
