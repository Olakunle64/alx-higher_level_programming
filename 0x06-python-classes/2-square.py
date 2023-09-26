#!/usr/bin/python3

"""This file is that contains a class called Square

    It has the special method and one field
    """


class Square:
    """This class has the __init__ method

    Attributes:
        ___init__: first method

    end

    """
    def __init__(self, size = 0):
        """Initializing self as a private attribute
        
        Args:
            size: an integer(ensure it is an integer and also
            it must not be less than 0)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
