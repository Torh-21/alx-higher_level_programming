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
    
    def __init__(self, width, height, x=0, y=0, id=None):
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

    @property
    def height(self):
        """
            returns the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            sets the height of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
            returns the x-coordinate of the Rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            sets the x-coordinate of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
            sets the y-coordinate of the Rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            sets the y-coordinate of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
            returns the area of the Rectangle
        """
        return self.width * self.height
