#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns a list of attributes and methods of the object.
    """
    return dir(obj)
