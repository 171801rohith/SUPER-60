# Problem Statement 3: Salary Class
# 1. Create a Salary class.
# 2. Attributes: basic, hra, allowance.
# 3. Add a method to compute the total salary (basic + hra + allowance).
# 4. Modify the Console class to print basic, hra, allowance, and total salary


class Salary:
    def __init__(self, basic, hra, allowance):
        self.basic = basic
        self.hra = hra
        self.allowance = allowance

    def get_total_salary(self):
        return self.basic + self.allowance + self.hra