#!/usr/bin/python3
"""This module contains the testcases for the class
    called <Rectangle>
    """


from models.rectangle import Rectangle
import unittest
from io import StringIO
import sys

class Test_Rectangle(unittest.TestCase):
    """The following methods contains the
    test cases for the class <Rectangle>
    """
    def test_a_incomplete_args(self):
        """define a class with incomplete arguments"""

        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(TypeError):
            r2 = Rectangle(2)
        r3 = Rectangle(2, 4)
        self.assertEqual(r3.id, 1)
        self.assertEqual(r3.x, 0)
        r3.x = 32
        self.assertEqual(r3.x, 32)
        self.assertEqual(r3.y, 0)
        r3.y = 65
        self.assertEqual(r3.y, 65)
        self.assertEqual(r3.width, 2)
        r3.width = 34
        self.assertEqual(r3.width, 34)
        self.assertEqual(r3.height, 4)
        r3.height = 13
        self.assertEqual(r3.height, 13)
        r4 = Rectangle(5, 9)
        self.assertEqual(r4.id, 2)
        r4.id = 0

    def test_b_complete_args(self):
        """define a class with complete arguments"""
        R1 = Rectangle(2, 4, 5, 10, 11)
        self.assertEqual(R1.width, 2)
        self.assertEqual(R1.height, 4)
        self.assertEqual(R1.x, 5)
        self.assertEqual(R1.y, 10)
        self.assertEqual(R1.id, 11)
        R1.id = 34
        self.assertEqual(R1.id, 34)
        R1.id = 0

    def test_args_type(self):
        """test the type of the arguments"""
        with self.assertRaises(TypeError) as errmsg:
            T1 = Rectangle("string", [2, 3])
        self.assertEqual(str(errmsg.exception), "width must be an integer")
        with self.assertRaises(TypeError) as errmsg:
            T1 = Rectangle(2, 4, "6", 7, 8)
        self.assertEqual(str(errmsg.exception), "x must be an integer")
        with self.assertRaises(TypeError) as errmsg:
            T1 = Rectangle(2, "height")
        self.assertEqual(str(errmsg.exception), "height must be an integer")
        with self.assertRaises(TypeError) as errmsg:
            T1 = Rectangle(2, 4, 6, "7")
        self.assertEqual(str(errmsg.exception), "y must be an integer")

    def test_value(self):
        """test for the value of each arguments"""
        with self.assertRaises(ValueError) as errmsg:
            V1 = Rectangle(0, 2)
        self.assertEqual(str(errmsg.exception), "width must be > 0")
        with self.assertRaises(ValueError) as errmsg:
            V1 = Rectangle(-2, 2)
        self.assertEqual(str(errmsg.exception), "width must be > 0")
        with self.assertRaises(ValueError) as errmsg:
            V1 = Rectangle(2, 0)
        self.assertEqual(str(errmsg.exception), "height must be > 0")
        with self.assertRaises(ValueError) as errmsg:
            V1 = Rectangle(2, -2)
        self.assertEqual(str(errmsg.exception), "height must be > 0")
        with self.assertRaises(ValueError) as errmsg:
             V1 = Rectangle(2, 3, -2)
        self.assertEqual(str(errmsg.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as errmsg:
            V1 = Rectangle(2, 3, 5, -4)
        self.assertEqual(str(errmsg.exception), "y must be >= 0")

    def test_area(self):
        """test the area of the rectangle"""
        A1 = Rectangle(2, 4, 5, 6, 7)
        A2 = Rectangle(4, 5)
        A3 = Rectangle(5, 5, 0, 0, 7)
        self.assertEqual(A1.area(), 8)
        self.assertEqual(A2.area(), 20)
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
        d1 = Rectangle(5, 2, 0, 0, 4)
        expected_output = "#####\n#####\n"
        self.assertEqual(Test_Rectangle.display_output(d1), expected_output)
        d2 = Rectangle(2, 4, 0, 0, 4)
        expected_output = "##\n##\n##\n##\n"
        self.assertEqual(Test_Rectangle.display_output(d2), expected_output)
        d3 = Rectangle(4, 2, 3, 2, 5)
        expected_output = "\n\n  ####\n  ####\n"
        self.assertEqual(self.display_output(d3), expected_output)
        d4 = Rectangle(4, 2, 3, 0, 5)
        expected_output = "\n\n####\n####\n"
        self.assertEqual(Test_Rectangle.display_output(d4), expected_output)

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
        s1 = Rectangle(1, 2, 3, 4, 5)
        expected_output = "[Rectangle] (5) 3/4 - 1/2\n"
        self.assertEqual(Test_Rectangle.p_str(s1), expected_output)
        s1 = Rectangle(5, 5, 1, 2)
        expected_output = "[Rectangle] (1) 1/2 - 5/5\n"
        #self.assertEqual(Test_Rectangle.p_str(s1), expected_output)
        s1 = Rectangle(5, 5)
        expected_output = "[Rectangle] (2) 0/0 - 5/5\n"
        #self.assertEqual(Test_Rectangle.p_str(s1), expected_output)
