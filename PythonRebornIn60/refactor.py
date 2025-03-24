# Exercise 6: Refactoring for Encapsulation
# Objective: Reinforce encapsulation by refactoring a class to use private variables and methods.

# Instructions:
# Start with this Person class that uses direct access:
# class Person:
#     def _init_(self, age, age):
#         self.name = name
#         selfage = age

# Refactor it to:
# Make name and age private (e.g., __name, __age).
# Add getter methods get_name() and get_age().
# Add setter methods set_name() and set_age(), with set_age() ensuring the age is a positive integer.


class Person:
    def _init_(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def set_age(self, age):
        if age < 0:
            raise Exception("Error: Age should be positive.")
        self.__age = age


def main():
    person = Person()
    person.set_name = "Rohith"
    person.set_age = 19

    print("Name:", person.name)
    print("Age:", person.age)

if __name__ == "__main__":
    main()
