#!/usr/bin/python3
"""Defines a MyList class that inherits from list."""


class MyList(list):
    """A class that inherits form list and includes a method to print"""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
