# Problem Statement 2:
# Address Class
# 1. Create an Address class.
# 2. Attributes: line1, line2, city, state, pin.
# 3. Add setter and getter methods for each attribute.
# 4. Establish a "has-a" relationship: Employee has an Address.
# 5. Create a Console class to print all details of the employee and address.


class Address:
    def __init__(self, line1, line2, city, state, pin):
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.state = state
        self.pin = pin

    def set_line1(self, line1):
        self.line1 = line1

    def set_line2(self, line2):
        self.line2 = line2

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_pin(self, pin):
        self.pin = pin

    def get_pin(self):
        return self.pin

    def get_state(self):
        return self.state

    def get_city(self):
        return self.city

    def get_line1(self):
        return self.line1

    def get_line2(self):
        return self.line2
