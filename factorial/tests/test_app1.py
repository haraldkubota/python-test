import unittest

import sys
from app.factorial import factorial

DEBUG = False

class MathTestCase(unittest.TestCase):
    def setUp(self):
        """Setting a variable which is part of all tests
        """
        self.version = "1.0.0"

    def tearDown(self):
        self.version = None

    def test_version(self):
        """Check that setUp() worked
        """
        self.assertEqual(self.version, "1.0.0")

    def test_factorial4(self):
        self.assertEqual(factorial(4), 24)

    @unittest.skip("Demonstrating skipping")
    def test_factorial5(self):
        self.assertTrue(factorial(5) == 120)

    @unittest.skipIf(DEBUG, "Don't test this when debugging")
    def test_factorial6(self):
        self.assertTrue(factorial(6) == 720)


if __name__ == '__main__':
    unittest.main()
