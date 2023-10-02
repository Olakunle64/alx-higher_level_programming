#!/usr/bin/python3
"""This module contains a class named <Rectangle>

    <Rectangle> has two instance variable with their
    respective getters and setters(@property)

    Methods: area() and perimeter() and the special
    methods known as __str__, __repr__ and __del__
    """


class Rectangle:
    """A class called <Rectangle>

    instance variable: width and height(with
    respective getters and setters)

    Class variable: number_of_instances

    Methods:
        area(): to get the area of the rectangle
        perimeter(): to get the perimeter of the rectangle
        __str__: string implementation
        __repr__: string implementation that can be parsed back to
        an instance
        __del__: print a messeage when an instance is deleted
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialization of the two instance variables"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """a getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """a setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """a getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """a setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of a rectangle"""
        if not self.__width or not self.__height:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """return the string implementation of the instance"""
        if not self.__width or not self.__height:
            return ""
        new_string = []
        for i in range(self.__height):
            new_string.append(str("#" * self.__width))
            if i != self.__height - 1:
                new_string.append(str("\n"))
        return "".join(new_string)

    def __repr__(self):
        """return the the string implementation that can be parsed
            back to an instance"""
        r = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return r

    def __del__(self):
        """print a message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
