# calculator.py
# Командная разработка калькулятора на Python

import math

class Calculator:
    def __init__(self):
        self.memory = 0.0
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero!")
        return a / b

    def power(self, base, exponent):
        return base ** exponent
    
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Modulo by zero!")
        return a % b

    def sine(self, x):
        return math.sin(x)
    
    def cosine(self, x):
        return math.cos(x)

    def memory_store(self, value):
        self.memory = value
    
    def memory_recall(self):
        return self.memory

    # Финальные функции
    def square_root(self, x):
        if x < 0:
            raise ValueError("Square root of negative number!")
        return math.sqrt(x)
    
    def floor(self, x):
        return math.floor(x)
    
    def ceil(self, x):
        return math.ceil(x)

if __name__ == "__main__":
    calc = Calculator()
    print("=== Python Calculator Team ===")
    print("Доступно: +, -, *, /, %, **, sin, cos, sqrt, floor, ceil, память")
    
    # Демонстрация всех функций
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"2 ** 8 = {calc.power(2, 8)}")
    print(f"17 % 5 = {calc.modulo(17, 5)}")
    print(f"sqrt(25) = {calc.square_root(25)}")
    print(f"floor(3.7) = {calc.floor(3.7)}")
    print(f"ceil(3.2) = {calc.ceil(3.2)}")
    print(f"sin(π/2) = {calc.sine(math.pi/2):.2f}")
    
    calc.memory_store(100)
    print(f"Память: {calc.memory_recall()}")
