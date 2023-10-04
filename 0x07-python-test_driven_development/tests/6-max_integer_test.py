#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """This class has only one method with several test cases"""

    def test_maxinteger(self):
        self.assertEqual(max_integer([2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([-2, -3, -4]), -2)
        self.assertEqual(max_integer([0]), 0)
