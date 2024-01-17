#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """
    Returns:
    list: A list of strings representing the attributes 
    and methods of the object.
    """
    return dir(obj)
