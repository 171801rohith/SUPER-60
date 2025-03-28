# Exercise : Diamond Inheritance Problem
# Objective
# Understand the diamond inheritance problem and Python’s resolution mechanism.
 
# Instructions
# Create a diamond-shaped class hierarchy:
# Base class A with greet(self) printing "Hello from A."
# Subclass B inherits from A, overrides greet(self) to print "Hello from B."
# Subclass C inherits from A, overrides greet(self) to print "Hello from C."
# Subclass D inherits from both B and C.
# In a main() function:
# Create a D object
# Call greet() on it.
# Observe which greet() is called and explain why.

class A:
    def greet(self):
        print("Hello from A")


class B(A):
    def greet(self):
        print("Hello from B")  


class C(A):
    def greet(self):
        print("Hello from C")  

class D(B, C):
    pass


if __name__ == "__main__":
    d = D()
    d.greet()
    print(help(D))