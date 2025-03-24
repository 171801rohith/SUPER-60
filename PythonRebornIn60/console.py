from employee import Employee
from address import Address
from salary import Salary
from employment import Empolyment
from hiring import Hiring


class Console:
    def get_details(self):
        print("Name:", self.emp.getName())
        print("Age", self.emp.getAge())
        print("Experience:", self.emp.getExperienceInYears())
        self.emp.getAddress()
        self.emp.getSalary()
        self.emp.getEmployment()
        self.hire.process_duration()

    def set_details(self, emp, hire):
        self.emp = emp
        self.hire = hire


console = Console()
add = Address("marnami", "bondel", "mangalore", "karnataka", 576599)
money = Salary(20030, 7000, 4533)
empment = Empolyment("2023-03-31", 89)
emp = Employee("Shek", 19, "4.5", add, money, empment)
hire = Hiring(23, 3, 6, 7)

console.set_details(emp, hire)
console.get_details()
