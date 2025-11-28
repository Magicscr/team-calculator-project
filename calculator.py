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

    # Тригонометрия от Alice
    def sine(self, x):
        import math
        return math.sin(x)
    
    def cosine(self, x):
        import math
        return math.cos(x)

if __name__ == "__main__":
    calc = Calculator()
    print("=== Калькулятор на Python ===")
    print("Доступно: +, -, *, /, %, **, sin, cos")
    # Alice изменила этот блок
    result = calc.add(10, 5)
    print(f"Пример: 10 + 5 = {result}")
