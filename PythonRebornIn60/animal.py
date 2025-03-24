# Exercise 1: Basic Inheritance with Animals
# Objective: Learn how to create a subclass that inherits from a base class and adds new attributes and methods.

# Instructions:
# Create a base class Animal with:
# An instance variable name.
# A constructor init(self, name) to set the name.
# A method speak(self) that prints "Unknown sound."
# Create a subclass Dog that inherits from Animal and:
# Adds an instance variable breed.
# Overrides the speak(self) method to print "Woof!"
# Adds a method fetch(self) to print "<name> is fetching the ball."
# In the main() function:
# Create a Dog object with name "Buddy" and breed "Golden Retriever."
# Call the speak() and fetch() methods on the dog object.
# Print the dog's name using the name attribute inherited from Animal.


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Unkown sound.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("Woof!")

    def fetch(self):
        print(f"{self.name} a {self.breed} is fetching the ball.")


def main():
    dog = Dog("Buddy", "Golden Retriever")
    print(dog.name)
    dog.speak()
    dog.fetch()


if __name__ == "__main__":
    main()
