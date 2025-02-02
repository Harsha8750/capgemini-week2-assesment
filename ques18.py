from abc import ABC, abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self, a, b):
        pass

    @abstractmethod
    def subtract(self, a, b):
        pass

    @abstractmethod
    def multiply(self, a, b):
        pass

    @abstractmethod
    def divide(self, a, b):
        pass

class BasicCalculator(ICalculator):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

calculator = BasicCalculator()
print(f"Add: {calculator.add(5, 3)}")
print(f"Subtract: {calculator.subtract(5, 3)}")
print(f"Multiply: {calculator.multiply(5, 3)}")
print(f"Divide: {calculator.divide(5, 3)}")
