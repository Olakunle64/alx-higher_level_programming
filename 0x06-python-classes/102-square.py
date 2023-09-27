#!/usr/bin/python3

"""This file is that contains a class called Square

    It has the special method and one field
    """


class Square:
    """This class has the __init__ method

    Attributes:
        ___init__: first method
        area: second method which is a public method
        getter: a getter
        setter: a setter

    other special methods are also included in the class

    """
    def __init__(self, size=0):
        """Initializing self as a private attribute

        Args:
            size: an integer(ensure it is an integer and also
            it must not be less than 0)
        """
        self.__size = size

    @property
    def size(self):
        """a getter to get the value of the private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """a setter to set the private attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of a square"""
        return (self.__size ** 2)

    def __eq__(self, other):
        """equal comparision"""
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """not equal to comparision"""
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __gt__(self, other):
        """greater than comparision"""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """greater than or equal to comparision"""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """less than comparision"""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """less than or equal to comparision"""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
