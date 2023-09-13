#!/usr/bin/python3


"""
    This function returns an object (Python data structure)
    represented by a JSON string
    This module defines the prototype def from_json_string(my_str):
"""
import json


def from_json_string(my_str):
    """
        This function returns an object represented by a JSON
        string
    """
    return json.loads(my_str)
