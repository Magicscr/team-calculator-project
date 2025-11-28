# test_calculator.py
import unittest
import math
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2.0)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8.0)
        self.assertEqual(self.calc.power(5, 0), 1.0)
    
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(7, 3), 1)
        with self.assertRaises(ValueError):
            self.calc.modulo(5, 0)
    
    def test_square_root(self):
        self.assertEqual(self.calc.square_root(25), 5.0)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
    
    def test_trigonometry(self):
        self.assertAlmostEqual(self.calc.sine(math.pi/2), 1.0, places=2)
        self.assertAlmostEqual(self.calc.cosine(0), 1.0, places=2)
    
    def test_floor_ceil(self):
        self.assertEqual(self.calc.floor(3.7), 3)
        self.assertEqual(self.calc.ceil(3.2), 4)
    
    def test_memory(self):
        self.calc.memory_store(100)
        self.assertEqual(self.calc.memory_recall(), 100)

if __name__ == '__main__':
    unittest.main()
