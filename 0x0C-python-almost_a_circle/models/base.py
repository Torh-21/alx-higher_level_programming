#!/usr/bin/python3


"""
    This module defines the class Base
"""


class Base:
    """
        This is the class Base which defines the
        private class attribute __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            initialization method for the Base class
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
