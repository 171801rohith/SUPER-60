# Problem Statement 4: Employment Class
# 1. Create an Employment class.
# 2. Attributes: date_of_joining, notice_period (default: 90 days).
# 3. Establish a "has-a" relationship: Employee has an Employment.
# 4. Modify the Console class to print experience in years (use the rule: if fractional part is .10 or .11, round up to the next year).

class Empolyment:
    def __init__(self, date_of_joining, notice_period=90):
        self.date_of_joining = date_of_joining
        self.notice_period = notice_period

    def get_employment_details(self):
        print("Date_Of_Joinig:", self.date_of_joining)
        print("Notice_Period:", self.notice_period)