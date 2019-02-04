# this is a second test file to see if pipline is running
import unittest
from test_1 import add

class First_test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,3), 4)
    def test_add2(self):
        self.assertNotEqual(add(2,4), 123)
    def failing_test(self):
        self.assertEqual(add(1,4),9)