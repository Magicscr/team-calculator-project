import unittest
import math
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(7, 0), 7)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(1000, 2000), 3000)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(8, 0), 8)
        self.assertEqual(self.calc.subtract(5, 8), -3)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(5000, 2000), 3000)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 4), 20)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(7, 0), 0)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(100, 50), 5000)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(15, 3), 5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(6, -3), -2)
        self.assertEqual(self.calc.divide(1000, 10), 100)
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(3, 2), 9)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(0, 5), 0)
        self.assertEqual(self.calc.power(-2, 3), -8)
        self.assertEqual(self.calc.power(-2, 2), 4)
        self.assertEqual(self.calc.power(10, 3), 1000)
    
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(7, 3), 1)
        self.assertEqual(self.calc.modulo(10, 5), 0)
        self.assertEqual(self.calc.modulo(0, 5), 0)
        self.assertEqual(self.calc.modulo(-7, 3), 2)
        self.assertEqual(self.calc.modulo(100, 30), 10)
        with self.assertRaises(ValueError):
            self.calc.modulo(5, 0)
    
    def test_square_root(self):
        self.assertEqual(self.calc.square_root(25), 5)
        self.assertEqual(self.calc.square_root(9), 3)
        self.assertEqual(self.calc.square_root(0), 0)
        self.assertEqual(self.calc.square_root(10000), 100)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
    
    def test_trigonometry(self):
        self.assertEqual(self.calc.sine(0), 0)
        self.assertEqual(self.calc.cosine(0), 1)
        # Используем almostEqual для сравнения с плавающей точкой
        self.assertAlmostEqual(self.calc.sine(math.pi/2), 1, places=10)
        self.assertAlmostEqual(self.calc.sine(math.pi), 0, places=10)
        self.assertAlmostEqual(self.calc.cosine(math.pi), -1, places=10)
    
    def test_floor_ceil(self):
        self.assertEqual(self.calc.floor(3.7), 3)
        self.assertEqual(self.calc.ceil(3.2), 4)
        self.assertEqual(self.calc.floor(5), 5)
        self.assertEqual(self.calc.ceil(5), 5)
        self.assertEqual(self.calc.floor(-3.7), -4)
        self.assertEqual(self.calc.ceil(-3.2), -3)
        self.assertEqual(self.calc.floor(123.9), 123)
        self.assertEqual(self.calc.ceil(123.1), 124)
    
    def test_memory(self):
        self.calc.memory_store(100)
        self.assertEqual(self.calc.memory_recall(), 100)
        self.calc.memory_store(0)
        self.assertEqual(self.calc.memory_recall(), 0)
        self.calc.memory_store(-50)
        self.assertEqual(self.calc.memory_recall(), -50)
        self.calc.memory_store(10000)
        self.assertEqual(self.calc.memory_recall(), 10000)

if __name__ == '__main__':
    unittest.main()
