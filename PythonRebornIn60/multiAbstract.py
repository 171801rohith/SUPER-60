# Exercise 3: Multiple Inheritance with Abstract Classes
# Objective
# Combine multiple inheritance with abstract classes for a flexible design.
# Instructions
# Create two abstract base classes:
# Flyer with an abstract method fly(self).
# Swimmer with an abstract method swim(self).
# Create a concrete class Duck that inherits from both Flyer and Swimmer:
# Implements fly(self) to print "Flying with wings."
# Implements swim(self) to print "Swimming with webbed feet."

# In a main() function:
# Create a Duck object.
# Call both fly() and swim() methods.

from abc import ABC, abstractmethod


class Flyer(ABC):
    @abstractmethod
    def fly(self):
        pass


class Swimmer(ABC):
    @abstractmethod
    def swim(self):
        pass


class Duck(Flyer, Swimmer):
    def fly(self):
        print("Flying with wings.")

    def swim(self):
        print("Swimming with webbed feet.")


def main():
    duck = Duck()


if __name__ == "__main__":
    main()
