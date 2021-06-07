
import unittest

from calculator import calculator


class testCase(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator()

    def test1(self):
        self.assertEqual(self.calculator.addition(10, 2), (12))

    def test2(self):
        self.assertEqual(self.calculator.subtraction(10, 5), (5))

    def test3(self):
        self.assertEqual(self.calculator.multiplication(10, 2), (20))

    def test4(self):
        self.assertEqual(self.calculator.division(10, 5), (2))

        
if __name__ == "__main__":
    unittest.main()
