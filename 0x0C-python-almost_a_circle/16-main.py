#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    s1 = Square(2, 4)
    Rectangle.save_to_file([s1, r2, r1])
    #Rectangle.save_to_file(None)

    with open("Rectangle.json", "r") as file:
        print(file.read())
