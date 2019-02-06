# this is a second test file to see if pipline is running
from test_1 import add
class TestClass(object):
    def test_one(self):
        assert add(1,3) == 5


