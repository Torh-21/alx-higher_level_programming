#!/usr/bin/python3


"""
    This function writes a string to a text file (UTF8) and
    returns the number of characters
    This module defines the functin def write_file(filename="", text=""):
"""


def write_file(filename="", text=""):
    """
        This function writes to the text file and returns the number
        of characters
    """
    with open(filename, "w", encoding="utf-8") as file:
        char_count = file.write(text)
    return char_count
