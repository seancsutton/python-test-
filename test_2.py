# this is a second test file to see if pipline is running
import unittest
from test_1 import add

class First_test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,4), 5)

suite = unittest.TestLoader().loadTestsFromTestCase(First_test)
unittest.TextTestRunner(verbosity=2).run(suite)