#!/usr/bin/python3


"""
    This function creates an Object from a “JSON file”
    This module defines the prototype def load_from_json_file(filename):
"""
import json


def load_from_json_file(filename):
    """
        This function creates an Object from a "JSON file"
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
