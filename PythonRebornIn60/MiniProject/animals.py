from abc import ABC, abstractmethod
import random


class Animals(ABC):
    def __init__(
        self,
        name,
        health_level,
        hunger,
        habitat_type,
    ):
        self._name = name
        self._health = health_level
        self._hunger = hunger
        self._habitat_type = habitat_type

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food_amount):
        pass

    def get_health(self):
        return self._health

    def get_hunger(self):
        return self._hunger

    def get_habitat_type(self):
        return self._habitat_type

    def decrease_health(self, amount):
        self._health = max(self._health - amount, 0)

    def decrease_hunger(self, amount):
        self._hunger = max(self._hunger - amount, 0)

    def increase_health(self, amount):
        self._health = min(self._health + amount, 100)

    def increase_hunger(self, amount):
        self._hunger = min(self._hunger + amount, 100)


class Lion(Animals):
    def __init__(self, name, health_level, hunger, habitat_type):
        super().__init__(name, health_level, hunger, habitat_type)

    def make_sound(self):
        print(f"{type(self).__name__} Roar!")

    def feed(self, food_amount):
        temp = self.get_hunger()
        self.decrease_hunger(food_amount * 2)
        self.increase_health(food_amount * 0.5)
        print(f"Feeding {type(self).__name__} {temp} -> {self.get_hunger()}")


class Elephant(Animals):
    def __init__(self, name, health_level, hunger, habitat_type):
        super().__init__(name, health_level, hunger, habitat_type)

    def make_sound(self):
        print(f"{type(self).__name__} Trumpet!")

    def feed(self, food_amount):
        temp = self.get_hunger()
        self.decrease_hunger(food_amount * 1.5)
        self.increase_health(food_amount * 0.3)
        print(f"Feeding {type(self).__name__} {temp} -> {self.get_hunger()}")


class Parrot(Animals):
    def __init__(self, name, health_level, hunger, habitat_type):
        super().__init__(name, health_level, hunger, habitat_type)

    def make_sound(self):
        print(f"{type(self).__name__} Squawk!")

    def feed(self, food_amount):
        temp = self.get_hunger()
        self.decrease_hunger(food_amount * 0.5)
        self.increase_health(food_amount * 0.2)
        print(f"Feeding {type(self).__name__} {temp} -> {self.get_hunger()}")
