# Exercise 2: Method Overriding with Vehicles
# Objective: Practice method overriding to change the behavior of a base class method in subclasses.

# Instructions:
# Create a base class Vehicle with:
# A method start_engine(self) that prints "Engine starting..."
# Create two subclasses:
# Car that overrides start_engine(self) to print "Car engine roaring to life!"
# ElectricCar that overrides start_engine(self) to print "Electric car engine silently humming."
# In the main() function:
# Create a list of vehicles: a Car and an ElectricCar.
# Iterate through the list and call start_engine() on each vehicle.


class Vehicle:
    def start_engine(self):
        print("Engine Starting...")


class Car(Vehicle):
    def start_engine(self):
        print("Car engine roaring to life!")


class ElectricCar(Vehicle):
    def start_engine(self):
        print("Electric car engine silently humming.")


def main():
    vehicles = [Car(), ElectricCar()]

    for vehicle in vehicles:
        vehicle.start_engine()


if __name__ == "__main__":
    main()
