# Exercise 2: Polymorphism with Shapes and Areas
# Objective: Calculate areas of different shapes using a polymorphic approach.

# Instructions:
# Create a base class Shape with a method area(self) that raises a NotImplementedError.
# Create two derived classes:
# Circle with an instance variable radius and implements area(self) to return π * radius².
# Square with an instance variable side and implements area(self) to return side².
# Write a function print_area(shape) that takes a Shape object and prints its area.
# In main(), create a list of shapes (a circle with radius 3 and a square with side 4), and use a loop to call print_area() on each.

import math


class Shapes:
    def area(self):
        raise NotImplementedError


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Square(Shapes):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


def print_area(shape):
    print(f"{type(shape).__name__}:", shape.area())


def main():
    shapes = [Circle(3), Square(4)]

    for shape in shapes:
        print_area(shape)


if __name__ == "__main__":
    main()
