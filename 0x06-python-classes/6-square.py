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
        my_print: a method that print a square

    end

    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializing self as a private attribute

        Args:
            size: an integer(ensure it is an integer and also
            it must not be less than 0)
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """a getter to get the value of the private attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """a setter to set the private attribute position"""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or not
            all(isinstance(x, int) and x >= 0 for x in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """return the area of a square"""
        return (self.__size ** 2)

    def my_print(self):
        """print a square with character <#> to stdout"""
        if self.__size == 0:
            print()
            return
        for yaxis in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for xaxis in range(self.__position[0]):
                print(' ', end='')
            for j in range(self.__size):
                print('#', end='')
            print()
