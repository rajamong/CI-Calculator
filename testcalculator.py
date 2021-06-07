# imports unittest functionality
import unittest
# imports calculator class from calculator program
from calculator import calculator

class testCase(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator()

    # tests the addition functionality
    def test1(self):
        self.assertEqual(self.calculator.addition(10, 2), (12))
    
    # tests the subtraction functionality
    def test2(self):
        self.assertEqual(self.calculator.subtraction(10, 5), (5))
    
    # tests the multiplication functionality
    def test3(self):
        self.assertEqual(self.calculator.multiplication(10, 2), (20))

    # tests the division functionality
    def test4(self):
        self.assertEqual(self.calculator.division(10, 5), (2))

if __name__ == "__main__":
    unittest.main()