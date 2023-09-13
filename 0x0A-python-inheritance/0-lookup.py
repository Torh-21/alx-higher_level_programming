#!/usr/bin/python3


"""
    This module defines the prototype def lookup(obj):
"""


def lookup(obj):
    """
        This function returns a list of available
        attributes and methods of an object.
    """
    return dir(obj)
