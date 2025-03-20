class Calculator:

    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y
        return self.result

    def subtract(self, x, y):
        self.result = x - y
        return self.result

    def multiply(self, x, y):
        self.result = x * y
        return self.result

    def divide(self, x, y):
        if y != 0:
            self.result = x / y
        else:
            print("Error: Division by zero is not allowed")
        return self.result

# Example usage:
calc = Calculator()
print(calc.add(5, 3))      # Output: 8
print(calc.subtract(10, 4))   # Output: 6
print(calc.multiply(7, 2))   # Output: 14
print(calc.divide(10, 0))    # Output: Error: Division by zero is not allowed
