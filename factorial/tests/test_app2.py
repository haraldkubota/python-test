import unittest

import sys
from app.factorial import factorial

class MoreMathTestCase(unittest.TestCase):
    def setUp(self):
        self.version = "1.0.0"
    def tearDown(self):
        self.version = None

    def test_factorial7(self):
        self.assertEqual(factorial(7), 5040)

    def test_factorial24(self):
    	"""Testing a large number > 2**64
    	"""
    	self.assertEqual(factorial(24), 620448401733239439360000)

