#!/usr/bin/python3


"""
    This functin writes an Object to a text file,
    using a JSON representation
    This module defines the prototype def save_to_json_file(my_obj, filename):
"""
import json


def save_to_json_file(my_obj, filename):
    """
        This function writes an Object to a text file,
        using JSON
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
