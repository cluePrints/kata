import unittest
from calculator import add

class Test(unittest.TestCase):
    def test_returns_zero_for_empty_str(self):
        self.assertEquals(0, add(""))

if __name__ == '__main__':
    unittest.main()
