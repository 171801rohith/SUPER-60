# Exercise 1: Polymorphism with Animal Sounds
# Objective: Use polymorphism to handle different animal sounds through a common interface.

# Instructions:
# Create a base class Animal with a method speak(self) that raises a NotImplementedError.
# Create three derived classes:
# Dog that overrides speak(self) to return "Woof!"
# Cat that overrides speak(self) to return "Meow!"
# Cow that overrides speak(self) to return "Moo!"
# Write a function make_sound(animal) that takes an Animal object and prints its sound using speak().
# In main(), create a list of animals (a dog, a cat, and a cow), and use a loop to call make_sound() on each.


class Animal:
    def speak(self):
        raise NotImplementedError


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Cow(Animal):
    def speak(self):
        return "Moo!"


def make_sound(animal):
    print(f"{type(animal).__name__}:", animal.speak())


def main():
    dog = Dog()
    cat = Cat()
    cow = Cow()

    animals = [dog, cat, cow]

    for animal in animals:
        make_sound(animal)


if __name__ == "__main__":
    main()
