#!/usr/bin/python3


"""
    This function returns the JSON representation of an
    object (string)
    This module defines the function def to_json_string(my_obj):
"""
import json


def to_json_string(my_obj):
    """
        This function returns the JSON representation of an
        object (string)
    """
    return json.dumps(my_obj)
