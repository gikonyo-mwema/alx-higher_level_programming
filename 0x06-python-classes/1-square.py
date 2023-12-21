#!/usr/bin/python3
"""A module for a square"""


class Square:
    """
    This class represents a square.
    It has a private instnce attribut: size.
    """
    def __init__(self, size):
        """
        Initializes the square.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
