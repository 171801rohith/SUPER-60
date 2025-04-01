# Project Overview In this wildlife sanctuary: Animals (e.g., Lion, Elephant, Parrot) have unique needs and behaviors.
# Habitats (e.g., Savanna, Jungle, Aviary) affect animal well-being and require maintenance.
# Staff (e.g., Caretaker, Veterinarian) perform specific tasks on animals and habitats.
# A Sanctuary class manages all entities and simulates a day in the sanctuary’s operations.

# Mini Project:
# Wildlife Sanctuary Management System with OOP Principles Objective
# Create a Python-based wildlife sanctuary management system that demonstrates Encapsulation, Inheritance, Polymorphism, and Abstraction.
# The system will manage different types of animals, their habitats, and staff responsibilities,
# simulating daily operations such as feeding, health checks, and habitat maintenance. This project adds complexity through multiple class hierarchies, interactions between objects, and dynamic simulation elements.

# Instructions 1.
# Abstract Base Class: Animal (Abstraction) Create an abstract base class Animal with: Protected Attributes: _name: The animal’s name (string). _health: Health level (0–100, float). _hunger: Hunger level (0–100, float). _habitat_type: The type of habitat required (string, e.g., "Savanna").
# Abstract Methods: make_sound(self): Defines the animal’s unique sound. feed(self, food_amount): Defines how the animal eats and updates hunger/health.
# Concrete Methods: get_health(), get_hunger(), get_habitat_type(): Getters for protected attributes.
# decrease_health(self, amount): Reduces _health (with a minimum of 0). increase_hunger(self, amount): Increases _hunger (with a maximum of 100).

# 2.
# Animal Subclasses (Inheritance and Polymorphism) Create at least three subclasses of Animal: Lion: make_sound: Prints "Roar!".
# feed: Reduces _hunger by food_amount * 2 (lions eat a lot) and increases _health by food_amount * 0.5.
# Elephant: make_sound: Prints "Trumpet!". feed: Reduces _hunger by food_amount * 1.5 and increases _health by food_amount * 0.3.
# Parrot: make_sound: Prints "Squawk!". feed: Reduces _hunger by food_amount * 0.5 (parrots eat less) and increases _health by food_amount * 0.2.

# 3. Abstract Base Class: Habitat (Abstraction)
# Create an abstract base class Habitat with:
# Protected Attributes:
# _type: Habitat type (string, e.g., "Savanna").
# _condition: Condition level (0–100, float, representing cleanliness/maintenance).
# _animals: List of animals in the habitat.
# Abstract Method:
# affect_animal(self, animal): Defines how the habitat impacts an animal’s health.
# Concrete Methods:
# add_animal(self, animal): Adds an animal if its _habitat_type matches.
# get_condition(): Getter for _condition.
# degrade(self, amount): Reduces _condition (e.g., due to animal activity).

# 4. Habitat Subclasses (Inheritance and Polymorphism)
# Create three subclasses of Habitat:
# o Savanna: affect_animal: If _condition > 50, increases animal health by5; otherwise, decreases by 5.
# o Jungle: affect_animal: If _condition > 60, increases health by 3; otherwise, decreases by 3.
# o Aviary: affect_animal: If _condition > 70, increases health by 2; otherwise, decreases by 2.

# 5. Abstract Base Class: Staff (Abstraction)
# • Create an abstract base class Staff with:
# o Protected Attributes:
# _name: Staff member’s name (string).
# _energy: Energy level (0–100, float).
# o Abstract Method:
# perform_task(self, target): Defines the staff’s specific action.
# o Concrete Methods:
# get_energy(): Getter for _energy.
# use_energy(self, amount): Reduces _energy (minimum 0).






import random
from animals import Animals, Elephant, Lion, Parrot
from habitat import Aviary, Habitat, Jungle, Savanna
from staff import Caretaker, Staff, Veterinarian


class Sanctuary:
    def __init__(
        self, animals: Animals = None, habitats: Habitat = None, staff: Staff = None
    ):
        self.animals = animals
        self.habitats = habitats
        self.staff = staff

    def add_anmial(self, animal: Animals, habitat: Habitat):
        if animal.get_habitat_type() == habitat._type:
            self.animals.append(animal)

    def add_habitat(self, habitat):
        self.habitats.append(habitat)

    def add_staff(self, staff):
        self.staff.append(staff)

    def simulate_day(self):
        for animal in self.animals:
            animal.make_sound()
            animal.increase_hunger(10)

        for habitat in self.habitats:
            habitat.degrade(10)

        print()
        print()

        for person in self.staff:
            if isinstance(person, Caretaker):
                habitat = random.choice(self.habitats)
                person.perform_task(habitat)
                print(f"Caretaker maintaining {type(habitat).__name__}")
            elif isinstance(person, Veterinarian):
                animal = random.choice(self.animals)
                if animal.get_health() < 50:
                    person.perform_task(animal)
                    print(
                        f"Veterinarian treating {type(animal).__name__} (health < 50)"
                    )

        print()
        print()

        for animal in self.animals:
            if animal.get_hunger() > 50:
                animal.feed(20)

        print()
        print()

        print("Animal Status: ")
        for animal in self.animals:
            print(
                f"{type(animal).__name__} ({animal.get_habitat_type()}): Health {animal.get_health()}, Hunger {animal.get_hunger()}"
            )

        print()
        print()

        print("Habitat Status: ")
        for habitat in self.habitats:
            print(f"{type(habitat).__name__}: Condition {habitat.get_condition()}")


def main():
    animals = [
        Lion("Leo", 10, 20, "Savanna"),
        Elephant("Mirchi", 90, 20, "Jungle"),
        Parrot("Chichi", 70, 45, "Aviary"),
    ]
    habitats = [
        Savanna(50, animals[0]),
        Jungle(75, animals[1]),
        Aviary(100, animals[2]),
    ]
    staff = [Caretaker("Shek", 50), Veterinarian("Aadithya", 85)]

    sanctuary = Sanctuary(animals, habitats, staff)
    print("--- Day 1 ---")
    sanctuary.simulate_day()
    print()
    print("--- Day 2 ---")
    sanctuary.simulate_day()


if __name__ == "__main__":
    main()
