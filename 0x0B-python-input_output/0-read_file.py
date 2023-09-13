#!/usr/bin/python3


"""
    This function reads a text file (UTF8) and prints it to stdout
    This module defines the prototype: def read_file(filename=""):
"""


def read_file(filename=""):
    """This function reads the content of a text file and prints it"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
