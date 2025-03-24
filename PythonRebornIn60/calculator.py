# Exercise 2: Abstraction with a Calculator Class
# Objective: Understand abstraction by designing a class with a simple interface that hides complex operations.
 
# Instructions:
# Create a Calculator class that performs basic arithmetic operations.
# Implement the following methods:
# _init_(self): Initializes an empty calculator (no instance variables needed yet).
# add(self, a, b): Returns the sum of a and b.
# subtract(self, a, b): Returns a minus b.
# multiply(self, a, b): Returns the product of a and b.
# divide(self, a, b): Returns a divided by b, but raises a ValueError if b is zero.

# Write a main function to:
# Create a Calculator object.
# Perform and print the results of: 5 + 3, 10 - 4, 6 * 2, and 8 / 2.
# Attempt to divide 10 by 0 and handle the exception.

class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try: 
            return a / b
        except Exception as e:
            return f"Error: {e}"
    
    def subtract(self, a, b):
        return a - b


def main():
    calc = Calculator()
    print("Add 5 + 3 =", calc.add(5, 3))
    print("Substract 10 - 4 =", calc.subtract(10, 4))
    print("Multiply 6 * 2 =", calc.multiply(6, 2))
    print("Divide 8 / 2 =", calc.divide(8, 2))
    print("Divide 10 / 0 =", calc.divide(10, 0))

if __name__ == "__main__":
    main()
