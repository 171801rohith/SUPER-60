# Exercise 2: Abstract Base Class for Shapes
# Objective
# Use abstract classes to define a common interface for different shapes.
# Instructions
# Import ABC and abstractmethod from the abc module.
# Create an abstract base class Shape with:
# An abstract method area(self).
# An abstract method perimeter(self).
# Create two concrete subclasses:
# Rectangle with instance variables width and height:
# area(self) returns width * height.
# perimeter(self) returns 2 * (width + height).
# Circle with instance variable radius:
# area(self) returns 3.1416 * radius ** 2.
# perimeter(self) returns 2 * 3.1416 * radius.

# In a main() function:
# Create a list of shapes: a rectangle (width 3, height 4) and a circle (radius 5).
# Iterate through the list and print each shape’s area and perimeter.

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return 2 * math.pi * self.radius
    

def main():
    shapes = [Rectangle(3, 4), Circle(5)]

    for shape in shapes:
        print(f"{type(shape).__name__} AREA: ", shape.area())
        print(f"{type(shape).__name__} PERIMETER: ", shape.perimeter())
        print("=" * 45)


if __name__ == "__main__":
    main()
