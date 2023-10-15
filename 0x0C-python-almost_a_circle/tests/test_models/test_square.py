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
        s3 = Square(2, 4, id=1)
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
        s4 = Square(5, 9, id=89)
        self.assertEqual(s4.id, 89)

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
        """test the display of the square"""
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
        """capture the display of the square to stdout"""
        with StringIO() as output:
            former_output = sys.stdout
            sys.stdout = output
            print(obj)
            sys.stdout = former_output
            return output.getvalue() 

    def test_str(self):
        """test string implementation of square"""
        s1 = Square(1, 3, 4, 5)
        expected_output = "[Square] (5) 3/4 - 1\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1 = Square(5, 5, 1, id=6)
        expected_output = "[Square] (6) 5/1 - 5\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1 = Square(6, 5, id=6)
        expected_output = "[Square] (6) 5/0 - 6\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
    def test_arbitrary_args(self):
        """test arbitrary arguments"""
        s1 = Square(3, 5, 6, 7)
        expected_output = "[Square] (7) 5/6 - 3\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1.update(89)
        expected_output = "[Square] (89) 5/6 - 3\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1.update(20, 21, 21)
        expected_output = "[Square] (20) 21/6 - 21\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1.update(1, 2, 2, 3, id=8)
        expected_output = "[Square] (1) 2/3 - 2\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1.update(1, 2, 2, 3, 4)
        expected_output = "[Square] (1) 2/3 - 2\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1.update()
        expected_output = "[Square] (1) 2/3 - 2\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1.update(9, 10, 11, 12, 13, 14, 15)
        expected_output = "[Square] (9) 11/12 - 10\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1.update(9, 43)
        expected_output = "[Square] (9) 11/12 - 43\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)

    def test_kwargs(self):
        """test arbitrary dictionary arguments"""
        s1 = Square(3, 4, 6, 7)
        expected_output = "[Square] (7) 4/6 - 3\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1.update(id=89)
        expected_output = "[Square] (89) 4/6 - 3\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1.update(id=20, size=21)
        expected_output = "[Square] (20) 4/6 - 21\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1.update(id=1, size=2, x=5)
        expected_output = "[Square] (1) 5/6 - 2\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1.update(id=1, size=2, x=4, y=5)
        expected_output = "[Square] (1) 4/5 - 2\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1.update(id=9, size=10, x=12, y=13)
        expected_output = "[Square] (9) 12/13 - 10\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)
        s1.update(89, id=9, width=16, height=15)
        expected_output = "[Square] (89) 12/13 - 10\n"
        self.assertEqual(Test_Square.p_str(s1), expected_output)

    def test_instance_attr(self):
        """test if the width and height has the same value"""
        s2 = Square(3, 4, 6, 5)
        expected_output = "[Square] (5) 4/6 - 3\n"
        self.assertEqual(Test_Square.p_str(s2), expected_output)
        s2.update(id=9, size=10, x=12, y=13)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.height, 10)
        s3 = Square(3, id=1)
        expected_output = "[Square] (1) 0/0 - 3\n"
        self.assertEqual(Test_Square.p_str(s3), expected_output)
        self.assertEqual(s3.size, 3)
        s3.size = 4
        self.assertEqual(s3.size, 4)
        self.assertEqual(s3.height, 4)
        self.assertEqual(s3.width, 4)

