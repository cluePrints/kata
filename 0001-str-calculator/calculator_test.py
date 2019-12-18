import unittest
from calculator import add


class Test(unittest.TestCase):
    def test_returns_zero_for_empty_str(self):
        self.assertEquals(0, add(""))

    def test_return_sum(self):
        self.assertEquals(5, add("2,3"))

    def test_return_one_number(self):
        self.assertEquals(2, add("2"))

    def test_return_anknown_amount_of_numbers(self):
        self.assertEquals(12, add("3,4,5"))
        self.assertEquals(25, add("3,4,5,13"))
        self.assertEquals(28, add("3,4,5,13,3"))

    def test_for_passing_other_symbols(self):
        self.assertEquals(6, add("1/n2,3"))


if __name__ == "__main__":
    unittest.main()
