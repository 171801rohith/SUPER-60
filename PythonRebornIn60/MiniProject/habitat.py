from abc import ABC, abstractmethod

from animals import Animals


class Habitat(ABC):
    def __init__(self, type, condition, animals=None):
        self._type = type
        self._condition = condition
        self._animals = animals

    @abstractmethod
    def affect_animal(self, animal):
        pass

    def add_animal(self, animal: Animals):
        if animal.get_habitat_type() == self._type:
            self._animals.append(animal)
        else:
            print(f"{animal._name} doesn't belong to {self._type}")

    def get_condition(self):
        return self._condition

    def degrade(self, amount):
        self._condition = max(self._condition - amount, 0)


class Savanna(Habitat):
    def __init__(self, condition, animals=None):
        super().__init__(type(self).__name__, condition, animals)

    def affect_animal(self, animal: Animals):
        if self._condition > 50:
            animal.increase_health(5)
        else:
            animal.decrease_health(5)


class Jungle(Habitat):
    def __init__(self, condition, animals=None):
        super().__init__(type(self).__name__, condition, animals)

    def affect_animal(self, animal: Animals):
        if self._condition > 60:
            animal.increase_health(3)
        else:
            animal.decrease_health(3)


class Aviary(Habitat):
    def __init__(self, condition, animals=None):
        super().__init__(type(self).__name__, condition, animals)

    def affect_animal(self, animal: Animals):
        if self._condition > 70:
            animal.increase_health(2)
        else:
            animal.decrease_health(2)