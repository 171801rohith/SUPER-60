from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, size):
        self.width = size
        self.height = size

    def calculate_area(self):
        return self.width * self.height


rectangle = Rectangle(12, 10)
square= Square(12)
print("Rectangel >>", rectangle.calculate_area())
print("Square >>", square.calculate_area())
