#!/usr/bin/python3


"""
    This function returns the dictionary description with
    simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object
    This module defines the prototype def class_to_json(obj):
"""


def class_to_json(obj):
    """
        This function returns the dict representation with
        simple data structure for JSON serialization of
        an object
    """
    return obj.__dict__
