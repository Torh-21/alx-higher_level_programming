#!/usr/bin/python3


"""
    This module contains the prototype def inherits_from(obj, a_class):
"""


def inherits_from(obj, a_class):
    """
        This function returns true if obj is a subclass
        of a_class, otherwise false
    """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
