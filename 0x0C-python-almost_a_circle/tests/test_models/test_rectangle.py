#!/usr/bin/python3
"""This module contains the testcases for the class
    called <Rectangle>
    """


import json
from models.rectangle import Rectangle
import unittest
from io import StringIO
import sys
from models.square import Square


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
        r3 = Rectangle(2, 4, id=1)
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
        r4 = Rectangle(5, 9, id=2)
        self.assertEqual(r4.id, 2)

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

    @staticmethod
    def display_output(obj):
        """capture the display of the rectangle to stdout"""
        with StringIO() as output:
            former_output = sys.stdout
            sys.stdout = output
            obj.display()
            sys.stdout = former_output
            return output.getvalue()

    def test_display(self):
        """test the display of the rectangle on stdout"""
        d1 = Rectangle(5, 2, 0, 0, 4)
        ex_out = "#####\n#####\n"
        self.assertEqual(Test_Rectangle.display_output(d1), ex_out)
        d2 = Rectangle(2, 4, 0, 0, 4)
        ex_out = "##\n##\n##\n##\n"
        self.assertEqual(Test_Rectangle.display_output(d2), ex_out)
        d3 = Rectangle(4, 2, 3, 2, 5)
        ex_out = "\n\n   ####\n   ####\n"
        self.assertEqual(self.display_output(d3), ex_out)
        d4 = Rectangle(4, 2, 3, 0, 5)
        ex_out = "   ####\n   ####\n"
        self.assertEqual(self.display_output(d4), ex_out)
        d5 = Rectangle(4, 2, y=3, x=0, id=5)
        ex_out = "\n\n\n####\n####\n"
        self.assertEqual(self.display_output(d5), ex_out)

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
        """test the string implementation of rectangle"""
        s1 = Rectangle(1, 2, 3, 4, 5)
        ex_out = "[Rectangle] (5) 3/4 - 1/2\n"
        self.assertEqual(Test_Rectangle.p_str(s1), ex_out)
        s1 = Rectangle(5, 5, 1, 2, 1)
        ex_out = "[Rectangle] (1) 1/2 - 5/5\n"
        self.assertEqual(Test_Rectangle.p_str(s1), ex_out)
        s1 = Rectangle(5, 5, id=2)
        ex_out = "[Rectangle] (2) 0/0 - 5/5\n"
        self.assertEqual(Test_Rectangle.p_str(s1), ex_out)

    def test_arbitrary_args(self):
        """test when abitrary arguments is given to the class"""
        r1 = Rectangle(3, 4, 5, 6, 7)
        ex_out = "[Rectangle] (7) 5/6 - 3/4\n"
        self.assertEqual(Test_Rectangle.p_str(r1), ex_out)
        r1.update(89)
        ex_out = "[Rectangle] (89) 5/6 - 3/4\n"
        self.assertEqual(Test_Rectangle.p_str(r1), ex_out)
        r1.update(20, 21)
        ex_out = "[Rectangle] (20) 5/6 - 21/4\n"
        self.assertEqual(Test_Rectangle.p_str(r1), ex_out)
        r1.update(1, 2, 3)
        ex_out = "[Rectangle] (1) 5/6 - 2/3\n"
        self.assertEqual(Test_Rectangle.p_str(r1), ex_out)
        r1.update(1, 2, 3, 4)
        ex_out = "[Rectangle] (1) 4/6 - 2/3\n"
        self.assertEqual(Test_Rectangle.p_str(r1), ex_out)
        r1.update(1, 2, 3, 4, 5)
        ex_out = "[Rectangle] (1) 4/5 - 2/3\n"
        self.assertEqual(Test_Rectangle.p_str(r1), ex_out)
        r1.update(9, 10, 11, 12, 13, 14, 15)
        ex_out = "[Rectangle] (9) 12/13 - 10/11\n"
        self.assertEqual(Test_Rectangle.p_str(r1), ex_out)

    def test_kwargs(self):
        """"test when a key-worded argument is given to the class"""
        r1 = Rectangle(3, 4, 5, 6, 7)
        ex_out = "[Rectangle] (7) 5/6 - 3/4\n"
        self.assertEqual(Test_Rectangle.p_str(r1), ex_out)
        r1.update(id=89)
        ex_out = "[Rectangle] (89) 5/6 - 3/4\n"
        self.assertEqual(Test_Rectangle.p_str(r1), ex_out)
        r1.update(id=20, width=21)
        ex_out = "[Rectangle] (20) 5/6 - 21/4\n"
        self.assertEqual(Test_Rectangle.p_str(r1), ex_out)
        r1.update(id=1, width=2, height=3)
        ex_out = "[Rectangle] (1) 5/6 - 2/3\n"
        self.assertEqual(Test_Rectangle.p_str(r1), ex_out)
        r1.update(id=1, width=2, height=3, x=4)
        ex_out = "[Rectangle] (1) 4/6 - 2/3\n"
        self.assertEqual(Test_Rectangle.p_str(r1), ex_out)
        r1.update(id=1, width=2, height=3, x=4, y=5)
        ex_out = "[Rectangle] (1) 4/5 - 2/3\n"
        self.assertEqual(Test_Rectangle.p_str(r1), ex_out)
        r1.update(id=9, width=10, height=11, x=12, y=13)
        ex_out = "[Rectangle] (9) 12/13 - 10/11\n"
        self.assertEqual(Test_Rectangle.p_str(r1), ex_out)
        r1.update(89, id=9, width=16, height=15)
        ex_out = "[Rectangle] (89) 12/13 - 10/11\n"
        self.assertEqual(Test_Rectangle.p_str(r1), ex_out)

    def test_obj_to_dict(self):
        """test if an instance is truly converted to a dictionary"""
        r1 = Rectangle(1, 2, id=8)
        ex_out = "[Rectangle] (8) 0/0 - 1/2\n"
        self.assertEqual(Test_Rectangle.p_str(r1), ex_out)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle(54, 78)
        r2 = Rectangle(**r1_dict)
        ex_out = "[Rectangle] (8) 0/0 - 1/2\n"
        self.assertEqual(Test_Rectangle.p_str(r2), ex_out)
        self.assertNotEqual(r1, r2)

    def test_json_string(self):
        """extract an instance from a json string"""
        r1 = Rectangle(1, 2, id=23)
        r1_dict = r1.to_dictionary()
        json_dict = Rectangle.to_json_string([r1_dict])
        ex_out = json.dumps(
                [{"width": 1, "height": 2, "x": 0, "y": 0, "id": 23}]) + '\n'
        self.assertEqual(Test_Rectangle.p_str(json_dict), ex_out)
        ex_out = "<class 'str'>\n"
        self.assertEqual(Test_Rectangle.p_str(type(json_dict)), ex_out)
        ex_out = "<class 'dict'>\n"
        self.assertEqual(Test_Rectangle.p_str(type(r1_dict)), ex_out)
        r2 = Rectangle(4, 5, 6, id=9)
        r2_dict = r2.to_dictionary()
        json_dict = Rectangle.to_json_string([r1_dict, r2_dict])
        ex_out = json.dumps([
            {"width": 1, "height": 2, "x": 0, "y": 0, "id": 23},
            {"width": 4, "height": 5, "x": 6, "y": 0, "id": 9}
        ]) + '\n'
        self.assertEqual(Test_Rectangle.p_str(json_dict), ex_out)

    def test_save_json_to_file(self):
        """test if truly json string representation is written to a file"""
        r1 = Rectangle(2, 4, id=89)
        r2 = Rectangle(3, 6, id=89)
        Rectangle.save_to_file([r1, r2])
        ex_out = json.dumps([
            {"width": 2, "height": 4, "x": 0, "y": 0, "id": 89},
            {"width": 3, "height": 6, "x": 0, "y": 0, "id": 89}
        ]) + '\n'
        with open("Rectangle.json", "r", encoding="utf-8") as file_obj:
            self.assertEqual(Test_Rectangle.p_str(file_obj.read()), ex_out)

    def test_from_json_string(self):
        """test if truly the original list is gotten from the json_string"""
        r1 = Rectangle(2, 4, id=89)
        r2 = Rectangle(3, 6, id=89)
        r1_dict = r1.to_dictionary()
        r2_dict = r2.to_dictionary()
        list_input = [r1_dict, r2_dict]
        json_string = Rectangle.to_json_string(list_input)
        json_list_output = Rectangle.from_json_string(json_string)
        ex_out = "<class 'list'>\n"
        self.assertEqual(Test_Rectangle.p_str(type(list_input)), ex_out)
        ex_out = "<class 'str'>\n"
        self.assertEqual(Test_Rectangle.p_str(type(json_string)), ex_out)
        ex_out = "<class 'list'>\n"
        self.assertEqual(Test_Rectangle.p_str(type(json_list_output)), ex_out)
        self.assertEqual(list_input, json_list_output)
        self.assertNotEqual(json_string, json_list_output)

    def test_instance_return(self):
        """test if truly an instance with all attributes set is returned"""
        r1 = Rectangle(2, 4, id=89)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        ex_out = "[Rectangle] (89) 0/0 - 2/4\n"
        self.assertEqual(Test_Rectangle.p_str(r1), ex_out)
        ex_out = "[Rectangle] (89) 0/0 - 2/4\n"
        self.assertEqual(Test_Rectangle.p_str(r2), ex_out)
        self.assertIsNot(r1, r2)

    def test_create_instance_from_file(self):
        """test if truly a list of an instance is returned"""
        r1 = Rectangle(10, 7, 2, 8)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle(2, 4)
        r2_dict = r2.to_dictionary()
        list_rectangle_input = [r1, r2]
        Rectangle.save_to_file(list_rectangle_input)
        retrived_rectangles = Rectangle.load_from_file()
        self.assertEqual(r1_dict, retrived_rectangles[0].to_dictionary())
        self.assertEqual(r2_dict, retrived_rectangles[1].to_dictionary())
