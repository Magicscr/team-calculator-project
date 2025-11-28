# calculator.py
# Командная разработка калькулятора на Python

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
        import math
        return math.sin(x)
    
    def cosine(self, x):
        import math
        return math.cos(x)

    def memory_store(self, value):
        self.memory = value
    
    def memory_recall(self):
        return self.memory

if __name__ == "__main__":
    calc = Calculator()
    # Alice меняет ЭТУ строку
    print("=== Калькулятор Python от Alice ===")
    print("Доступно: +, -, *, /, %, **, sin, cos, память")
    result = calc.add(10, 5)
    calc.memory_store(100)
    print(f"Пример: 10 + 5 = {result}")
    print(f"Память: {calc.memory_recall()}")
    print(f"sin(90) = {calc.sine(1.57):.2f}")
