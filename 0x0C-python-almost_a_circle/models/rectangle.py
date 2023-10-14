#!/usr/bin/python3
"""This module contains a class named <Rectangle>

    It has 4 private instance attribute and one method.
    Each private instance attribute has a getter and a setter.
    """


from models.base import Base

class Rectangle(Base):
    """The Rectangle class

    instance field:
        width: the width
        height: the height
        x: x
        y: y

    method: __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing the private attribute"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        #super().__init__(id)

    @property
    def width(self):
        """getter for the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter for the width"""
        if not isinstance(width, int):
            raise TypeError("{} must be an integer".format("width"))
        if width <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = width

    @property
    def height(self):
        """getter for the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter for the height"""
        if not isinstance(height, int):
            raise TypeError("{} must be an integer".format("height"))
        if height <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = height

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for x"""
        if not isinstance(x, int):
            raise TypeError("{} must be an integer".format("x"))
        if x < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for y"""
        if not isinstance(y, int):
            raise TypeError("{} must be an integer".format("y"))
        if y < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = y

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """print a rectangle with #"""
        print("\n" * self.__y, end='')
        for i in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """string implementation"""
        return str("[Rectangle] (" + str(self.id) + ") " + str(self.__x)
                + "/" + str(self.__y) + " - "
                + str(self.__width) + "/" + str(self.__height)
                )
