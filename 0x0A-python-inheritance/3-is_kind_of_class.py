#!/usr/bin/python3


"""
    This module defines the prototype def is_kind_of_class(obj, a_class):
"""


def is_kind_of_class(obj, a_class):
    """
        This function returns True if obj is an instance
        or inherited from a_class, else False
    """
    return (isinstance(obj, a_class))
