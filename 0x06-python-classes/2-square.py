#!/usr/bin/python3
"""A module for a square"""


class Square:
    """
    This class reprents a square.
    It has a private instance  attribut: size.
    """
    def __init__(self, size=0):
        """
        Initializes the square.
        Args:
            size (int, optional): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
