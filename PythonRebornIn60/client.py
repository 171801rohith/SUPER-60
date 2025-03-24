# Exercise 2: Client's View of a Subclass
# Objective: Understand how a subclass integrates base class and subclass functionality as a single unit from the client's perspective.

# Instructions:
# Using the Employee and Manager classes from your lesson:
# Ensure Employee has methods getName(), getTitle(), and payPerYear() (calculating hourly pay).
# Ensure Manager overrides payPerYear() (using salary and optional bonus) and adds getReports().
# In the main() function:
# Create an Employee object and a Manager object.
# Create a list containing both objects.
# Iterate through the list and call getName() and payPerYear() on each object.
# For the Manager object, call getReports() to print the list of reports.


class Employee:
    def __init__(self, name, title, hourly_rate, hours_per_week):
        self.name = name
        self.title = title
        self.hourly_rate = hourly_rate
        self.hours_per_week = hours_per_week

    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def payPerYear(self):
        return self.hourly_rate * self.hours_per_week * 52


class Manager(Employee):
    def __init__(self, name, title, salary, bonus=0, reports=None):
        super().__init__(name, title, 0, 0)  # Manager doesn't need hourly rate
        self.salary = salary
        self.bonus = bonus
        self.reports = reports if reports else []

    def payPerYear(self):
        return self.salary + self.bonus

    def getReports(self):
        return self.reports


def main():
    emp = Employee("Alice", "Engineer", 50, 40)
    mgr = Manager("Bob", "Director", 120000, 10000, ["Alice", "Charlie"])

    employees = [emp, mgr]

    for e in employees:
        print(f"Name: {e.getName()}, Annual Pay: {e.payPerYear()}")
        if isinstance(e, Manager):
            print(f"Reports: {e.getReports()}")


if __name__ == "__main__":
    main()
