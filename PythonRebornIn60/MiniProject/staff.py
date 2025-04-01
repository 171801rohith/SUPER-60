from abc import ABC, abstractmethod
from animals import Animals
from habitat import Habitat

 
class Staff(ABC):
    def __init__(self, name, energy):
        self._name = name
        self._energy = energy

    @abstractmethod
    def perform_task(self, target):
        pass

    def get_energy(self):
        return self._energy

    def use_energy(self, amount):
        self._energy = max(self._energy - amount, 0)


class Caretaker(Staff):
    def __init__(self, name, energy):
        super().__init__(name, energy)

    def perform_task(self, target):
        if isinstance(target, Habitat):
            target._condition = min(100, target._condition + 20)
            self.use_energy(10)
        else:
            print("Caretaker can only maintain habitats.")


class Veterinarian(Staff):
    def __init__(self, name, energy):
        super().__init__(name, energy)

    def perform_task(self, target):
        if isinstance(target, Animals):
            target.increase_health(15)
            self.use_energy(15)
        else:
            print("Veterinarian can only treat animals.")