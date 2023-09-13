#!/usr/bin/python3


"""
    This function appends a string to the end of a text file (UTF8)
    and returns the number of characters added
    This module defines the prototype def append_write(filename="", text=""):
"""

def append_write(filename="", text=""):
    """
        This function appends a string to the end of a text file
        and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        char_count = file.write(text)
    return char_count
