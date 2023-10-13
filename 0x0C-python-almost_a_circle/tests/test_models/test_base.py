#!/usr/bin/python3
"""This module is contains unittest to test a class called
    <Base>
    """


import unittest
#Base = __import__('../..base').Base
from models.base import Base

class Test_Base(unittest.TestCase):
    """Testcases for the function called <Base>"""

    def test_None_id(self):
        """test if id is None"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        b1.id = 17
        self.assertEqual(b1.id, 17)
    
    def test_id(self):
        """test when id is given"""
        b3 = Base(12)
        b4 = Base(20)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 20)
        b3.id = 24
        self.assertEqual(b3.id, 24)

    def test_get_class_attr(self):
        """test when trying to access the private class attr"""
        b1 = Base()
        with self.assertRaises(AttributeError):
            b1.__nb_objects
