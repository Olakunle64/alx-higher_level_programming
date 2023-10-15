#!/usr/bin/python3
"""This module contains the class called <Square>

    It inherit from the class called <Rectangle>
    """


from models.rectangle import Rectangle

class Square(Rectangle):
    """The class Square has two methods and several field
    attributes

    methods: __init__ and __str__
    instance field attribute:
        size: size
        x: x
        y: y
        id: id
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initializing the instance field attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """string implementation of square"""
        return ("[Square] (" + str(self.id) + ") "
                + str(self.x) + "/" + str(self.y) + " - " + str(self.size)
                )

    def update(self, *args, **kwargs):
        """if args exists, assign the value(s) to square attribute
        otherwise assign the value(s) of kwargs
        """
        i = 0
        flag = 0
        for arg in args:
            if i == 0:
                self.id = arg
                flag = 1
            elif i == 1:
                self.size = arg
            elif i == 2:
                self.x = arg
            elif i == 3:
                self.y = arg
            else:
                break
            i += 1
        if not flag:
            i = 0
            for key in kwargs.keys():
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.size = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]
                i += 1
                if i > 4:
                    break
