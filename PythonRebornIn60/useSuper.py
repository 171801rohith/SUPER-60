# Exercise 1: Using super() to Extend Functionality
# Objective: Use super() to call a base class method from a subclass and extend its functionality.
# Instructions:
# Create a base class Person with:
# Instance variables name and age.
# A constructor _init_(self, name, age) to set these variables.
# A method introduce(self) that prints "My name is <name> and I am <age> years old."
# Create a subclass Student that inherits from Person and:
# Adds an instance variable major.
# Overrides introduce(self) to first call the base class's introduce() method using super(), then prints "I am majoring in <major>."
# In the main() function:
# Create a Student object with name "Alice", age 20, and major "Computer Science."
# Call the introduce() method on the student object.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def introduce(self):
        intro = super().introduce()
        return f"{intro} I am majoring in {self.major}."
    

def main():
    stud = Student("Alice", 20, "Computer Science")
    print(stud.introduce())

if __name__ == "__main__":
    main()
