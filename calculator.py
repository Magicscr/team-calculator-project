# calculator.py
# Командная разработка калькулятора на Python

class Calculator:
    def __init__(self):
        self.memory = 0.0
    
    # Базовые операции (добавят разработчики)
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

if __name__ == "__main__":
    calc = Calculator()
    print("=== Калькулятор на Python ===")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"5 - 3 = {calc.subtract(5, 3)}")
