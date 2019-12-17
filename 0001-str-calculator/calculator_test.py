import unittest
from calculator import add


class Test(unittest.TestCase):
    def test_returns_zero_for_empty_str(self):
        self.assertEquals(0, add(""))

    def test_return_sum(self):
        self.assertEquals(5, add("2,3"))

    def test_return_one_number(self):
        self.assertEquals(2, add("2"))


if __name__ == "__main__":
    unittest.main()
