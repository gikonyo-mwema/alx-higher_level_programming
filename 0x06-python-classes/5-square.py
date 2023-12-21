#!/usr/bin/python3
"""A module for a square"""


class Square:
    """
    This class represents a square.
    It has a private iinstance attribute: size.
    """
    def __init__(self, size=0):
        """
        Initializes the square.
        Args:
            size (int, optional): the size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for size.
        Return:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size.
        Args:
            value (int): The size of the square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns th current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #.
        Prints an empty line if size is equal to 0.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
