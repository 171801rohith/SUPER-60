# Exercise 4: Inheritance with Bank Accounts
# Objective: Apply inheritance to create specialized bank account types with unique features.
 
# Instructions:
# Create a base class BankAccount with:
# Instance variables account_number and balance.
# A constructor _init_(self, account_number, initial_balance=0.0).
# Methods deposit(self, amount) to add to the balance and withdraw(self, amount) to subtract from the balance (if sufficient funds).
# A method get_balance(self) to return the current balance.
# Create a subclass SavingsAccount that inherits from BankAccount and:
# Adds an instance variable interest_rate.
# Adds a method add_interest(self) to increase the balance by the interest rate (e.g., balance += balance * interest_rate).
# Create a subclass CheckingAccount that inherits from BankAccount and:
# Adds an instance variable transaction_fee.
# Overrides withdraw(self, amount) to deduct an additional transaction_fee after a withdrawal.
# In the main() function:
# Create a SavingsAccount with account number "12345", initial balance 1000, and interest rate 0.02.
# Deposit 500, add interest, and print the balance.
# Create a CheckingAccount with account number "67890", initial balance 2000, and transaction fee 2.50.
# Withdraw 100, and print the balance (should deduct 100 + 2.50).

class BankAccount:
    def __init__(self, account_number, initial_balance=0.0):
        self.account_number = account_number
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdraw amount.")
        elif self.balance - amount < 0:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
        else:
            self.balance += amount

    def get_balance(self):
        return self.balance
    

class SavingsAccount(BankAccount):
    def __init__(self, account_number, initial_balance, interest_rate):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        self.balance += self.balance * self.interest_rate

class CheckingAccount(BankAccount):
    def __init__(self, account_number, initial_balance, transaction_fee):
        super().__init__(account_number, initial_balance)
        self.transaction_fee = transaction_fee
    
    def withdraw(self, amount):
        super().withdraw(amount)
        self.balance -= self.transaction_fee

def main():
    savings = SavingsAccount("12345", 1000, 0.02)
    savings.deposit(500)
    savings.add_interest()
    print(savings.get_balance())

    check = CheckingAccount("67890", 2000, 2.50)
    check.withdraw(100)
    print(check.get_balance())



if __name__ == "__main__":
    main()