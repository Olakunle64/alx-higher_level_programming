#!/usr/bin/python3
"""This module contains the testcases for the class
    called <Square>
    """


from models.square import Square
import unittest
from io import StringIO
import sys

class Test_Square(unittest.TestCase):
    """The following methods contains the
    test cases for the class <Square>
    """
    def test_a_incomplete_args(self):
        """define a class with incomplete arguments"""

        with self.assertRaises(TypeError):
            s1 = Square()
        s3 = Square(2, 4)
        self.assertEqual(s3.id, 1)
        self.assertEqual(s3.x, 4)
        s3.x = 32
        self.assertEqual(s3.x, 32)
        self.assertEqual(s3.y, 0)
        s3.y = 65
        self.assertEqual(s3.y, 65)
        self.assertEqual(s3.width, 2)
        s3.width = 34
        self.assertEqual(s3.width, 34)
        self.assertEqual(s3.height, 2)
        s3.height = 13
        self.assertEqual(s3.height, 13)
        s4 = Square(5, 9)
        self.assertEqual(s4.id, 2)
        s4.id = 0

    def test_b_complete_args(self):
        """define a class with complete arguments"""
        S1 = Square(2, 5, 10, 11)
        self.assertEqual(S1.width, 2)
        self.assertEqual(S1.height, 2)
        self.assertEqual(S1.x, 5)
        self.assertEqual(S1.y, 10)
        self.assertEqual(S1.id, 11)
        S1.id = 34
        self.assertEqual(S1.id, 34)
        S1.id = 0

    def test_args_type(self):
        """test the type of the arguments"""
        with self.assertRaises(TypeError) as errmsg:
            s1 = Square("string", [2, 3])
        self.assertEqual(str(errmsg.exception), "width must be an integer")
        with self.assertRaises(TypeError) as errmsg:
            s1 = Square(2, "6", 7, 8)
        self.assertEqual(str(errmsg.exception), "x must be an integer")
        with self.assertRaises(TypeError) as errmsg:
            s1 = Square("width")
        self.assertEqual(str(errmsg.exception), "width must be an integer")
        with self.assertRaises(TypeError) as errmsg:
            s1 = Square(2, 6, "7")
        self.assertEqual(str(errmsg.exception), "y must be an integer")

    def test_value(self):
        """test for the value of each arguments"""
        with self.assertRaises(ValueError) as errmsg:
            s1 = Square(0, 2)
        self.assertEqual(str(errmsg.exception), "width must be > 0")
        with self.assertRaises(ValueError) as errmsg:
            s1 = Square(-2, 2)
        self.assertEqual(str(errmsg.exception), "width must be > 0")
        with self.assertRaises(ValueError) as errmsg:
             s1 = Square(2, -2)
        self.assertEqual(str(errmsg.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as errmsg:
            s1 = Square(2, 5, -4)
        self.assertEqual(str(errmsg.exception), "y must be >= 0")

    def test_area(self):
        """test the area of the rectangle"""
        A1 = Square(2, 5, 6, 7)
        A2 = Square(4, 5)
        A3 = Square(5, 0, 0, 7)
        self.assertEqual(A1.area(), 4)
        self.assertEqual(A2.area(), 16)
        self.assertEqual(A3.area(), 25)
        A3.id = 0

    @staticmethod
    def display_output(obj):
        """test the display of the rectangle"""
        with StringIO() as output:
            former_output = sys.stdout
            sys.stdout = output
            obj.display()
            sys.stdout = former_output
            return output.getvalue()

    def test_display(self):
        d1 = Square(5, 0, 0, 4)
        expected_output = "#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(Test_Square.display_output(d1), expected_output)
        d2 = Square(2, 0, 0, 4)
        expected_output = "##\n##\n"
        self.assertEqual(Test_Square.display_output(d2), expected_output)
        d3 = Square(4, 3, 2, 5)
        expected_output = "\n\n   ####\n   ####\n   ####\n   ####\n"
        self.assertEqual(self.display_output(d3), expected_output)
        d4 = Square(2, 3, 0, 5)
        expected_output = "   ##\n   ##\n"

    @staticmethod
    def p_str(obj):
        """test the display of the rectangle"""
        with StringIO() as output:
            former_output = sys.stdout
            sys.stdout = output
            print(obj)
            sys.stdout = former_output
            return output.getvalue() 

    def test_str(self):
        s1 = Square(1, 3, 4, 5)
        expected_output = "[Square] (5) 3/4 - 1/1\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1 = Rectangle(5, 5, 1)
        expected_output = "[Square] (1) 5/1 - 5/5\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1 = Square(5, 5)
        expected_output = "[Square] (2) 5/0 - 5/5\n"
        elf.assertEqual(Test_Square.p_str(s1), expected_output)
    def test_arbitrary_args(self):
        s1 = Square(3, 5, 6, 7)
        expected_output = "[Square] (7) 5/6 - 3/3\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1.update(89)
        expected_output = "[Square] (89) 5/6 - 3/3\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1.update(20, 21, 21)
        expected_output = "[Square] (20) 5/6 - 21/21\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        r1.update(1, 2, 2, 3)
        expected_output = "[Square] (1) 3/6 - 2/2\n"
        self.assertEqual(Test_Square.p_str(r1), expected_output)
        r1.update(1, 2, 2, 3, 4)
        expected_output = "[Square] (1) 3/4 - 2/2\n"
        self.assertEqual(Test_Square.p_str(r1), expected_output)
        r1.update()
        expected_output = "[Square] (1) 3/4 - 2/2\n"
        self.assertEqual(Test_Square.p_str(r1), expected_output)
        r1.update(9, 10, 11, 12, 13, 14, 15)
        expected_output = "[Square] (9) 12/13 - 10/11\n"
        self.assertEqual(Test_Square.p_str(r1), expected_output)
        r1.update(9, 43)
        expected_output = "[Square] (9) 12/13 - 43/11\n"
        self.assertEqual(Test_Square.p_str(r1), expected_output)

    def test_kwargs(self):
        r1 = Square(3, 4, 6, 7)
        expected_output = "[Square] (7) 4/6 - 3/3\n"
        self.assertEqual(Test_Rectangle.p_str(r1), expected_output)
        r1.update(id=89)
        expected_output = "[Rectangle] (89) 4/6 - 3/3\n"
        self.assertEqual(Test_Rectangle.p_str(r1), expected_output)
        r1.update(id=20, width=21)
        expected_output = "[Rectangle] (20) 4/6 - 21/4\n"
        self.assertEqual(Test_Rectangle.p_str(r1), expected_output)
        r1.update(id=1, width=2, height=3)
        expected_output = "[Rectangle] (1) 4/6 - 2/3\n"
        self.assertEqual(Test_Rectangle.p_str(r1), expected_output)
        r1.update(id=1, width=2, height=3, x=5)
        expected_output = "[Rectangle] (1) 5/6 - 2/3\n"
        self.assertEqual(Test_Rectangle.p_str(r1), expected_output)
        r1.update(id=1, width=2, height=3, x=4, y=5)
        expected_output = "[Rectangle] (1) 4/5 - 2/3\n"
        self.assertEqual(Test_Rectangle.p_str(r1), expected_output)
        r1.update(id=9, width=10, height=11, x=12, y=13)
        expected_output = "[Rectangle] (9) 12/13 - 10/11\n"
        self.assertEqual(Test_Rectangle.p_str(r1), expected_output)
        r1.update(89, id=9, width=16, height=15)
        expected_output = "[Rectangle] (89) 12/13 - 10/11\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
