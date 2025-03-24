# Problem Statement 1: Employee Class
# 1. Create an Employee class.
# 2. Attributes: name (str), age (int), and experience (str).
# 3. Add setter and getter methods for each attribute.
# 4. Add a compute_years method to calculate experience in years.
#   a. Throw an InvalidExperienceException if the experience is not in the permissible range.
#   b. Permissible range:
#       i. Only 1 digit after . (e.g., 5.7).
#       ii. If 2 digits after ., they must be 10 or 11 (e.g., 5.10 or 5.11).
# 5. Add a rule to upgrade/downgrade experience:
#   a. If the fractional part is 10 or 11, upgrade the integer part by 1 (e.g., 5.10 → 6).
#   b. If the fractional part is a single digit, downgrade to the integer part (e.g., 4.7 → 4).

from address import Address
from salary import Salary
from employment import Empolyment


class InvalidExperienceException(Exception):
    def __init__(self, message="Experience is not in the permissible range"):
        super().__init__(message)


class Employee:
    def __init__(self, name="", age=0, experience="", address=None, money=None, employment=None):
        self.name = name
        self.age = age
        self.experience = experience
        self.address = address
        self.money = money
        self.employment = employment

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setExperience(self, experience):
        self.experience = experience

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getExperience(self):
        return self.experience

    def getAddress(self):
        print("Line1:", self.address.get_line1())
        print("Line2:", self.address.get_line2())
        print("State:", self.address.get_state())
        print("City:", self.address.get_city())
        print("Pin:", self.address.get_pin())

    def getSalary(self):
        print("Basic Salary:", self.money.basic)
        print("HRA:", self.money.hra)
        print("Allowance:", self.money.allowance)
        print("Total Salary:", self.money.get_total_salary())

    def getEmployment(self):
        self.employment.get_employment_details()

    def computeYears(self):
        list = self.experience.split(".")

        if len(list) == 1:
            list.append("0")

        if len(list[1]) > 1 and int(list[1]) < 10:
            raise InvalidExperienceException()
        elif int(list[1]) <= 9:
            self.experience = list[0]
        elif int(list[1]) <= 11:
            self.experience = str(int(list[0]) + 1)
        else:
            raise InvalidExperienceException()

        return self.experience

    def getExperienceInYears(self):
        return self.computeYears()


# add = Address("line1", "line2", "city", "state", 575001)

# emp1 = Employee("Abhishek", 100, "10.1", add)
# print(emp1.getAge())
# try:
#     print(emp1.getExperienceInYears())
# except InvalidExperienceException as e:
#     print("Exception :", e)

# emp1.getAddress()
