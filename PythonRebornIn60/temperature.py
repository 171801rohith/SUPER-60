# Exercise 3: Using Properties with a Temperature Class
# Objective: Explore encapsulation and abstraction using Python properties to control data access.

# Instructions:
# Create a Temperature class that stores temperature in Celsius.
# Use a private instance variable __celsius to hold the temperature.

# Implement properties to:
# Get and set the temperature in Celsius (property name: celsius).
# Get and set the temperature in Fahrenheit (property name: fahrenheit), converting to/from Celsius internally (F = C * 9/5 + 32; C = (F - 32) * 5/9).

# Write a main function to:
# Create a Temperature object with an initial Celsius value of 25.
# Print the temperature in both Celsius and Fahrenheit.
# Set the temperature to 98.6 Fahrenheit and print the new Celsius and Fahrenheit values.


class Temperature:
    __celsius = None

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def set_celsius(self, cel):
        self.__celsius = cel

    @property
    def fahrenheit(self):
        return self.__celsius * 9 / 5 + 32

    @fahrenheit.setter
    def set_fahrenheit(self, fah):
        self.__celsius = (fah - 32) * 5 / 9



def main():
    temp = Temperature()
    temp.set_celsius = 10
    print(temp.celsius)

    temp.set_fahrenheit = 28
    print(temp.celsius)
    print(temp.fahrenheit)

if __name__ == "__main__":
    main()