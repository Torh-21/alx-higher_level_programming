#!/usr/bin/python3


"""
    This script defines the Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
        This defines the Rectangle class
        which inherits from the Base class
    """
    
    def __init_(self, width, height, x=0, y=0, id=None):
        """
            This method initializes a new Rectangle
            Args:
                width (int): The width
                height (int): The height
                x (int): The x-coordinate
                y (int): The y-coordinate
                id (int): The identity
            Raises:
                TypeError: flagged when the width or height
                isn't an int
                ValueError: flagged when the width or height <= 0
                TypeError: flagged when x or y isn't an int
                ValueError: flagged when x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
            returns the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            sets the width of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

