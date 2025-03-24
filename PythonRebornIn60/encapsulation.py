# Exercise 1: Encapsulation with a BankAccount Class
# Objective: Practice encapsulation by creating a class with private data and controlled access through methods.

# Instructions:
# Create a BankAccount class with two private instance variable
# __account_number (a string)
# __balance (a float)

# Implement the following methods:
# _init_(self, account_number, initial_balance=0.0): Initializes the account with the given account number and an optional initial balance (defaulting to 0.0).
# get_account_number(self): Returns the account number.
# get_balance(self): Returns the current balance.
# deposit(self, amount): Adds the specified amount to the balance if the amount is positive; otherwise, prints "Invalid deposit amount."
# withdraw(self, amount): Subtracts the specified amount from the balance if the amount is positive and does not exceed the current balance; otherwise, prints "Insufficient funds" or "Invalid withdrawal amount" as appropriate.
# Write a main function to:
# Create a BankAccount object with account number "12345" and initial balance 100.0.
# Deposit 50.0 into the account.
# Withdraw 30.0 from the account.
# Attempt to withdraw 150.0 from the account.
# Print the account number and final balance.


class BankAccount:
    def __init__(self, account_number, initial_balance=0.0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_initial_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdraw amount.")
        elif self.__balance - amount < 0:
            print("Insufficient funds")
        else:
            self.__balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
        else:
            self.__balance += amount

    @property
    def get_details(self):
        print("ACCOUNT_NO:", self.__account_number)
        print("BALANCE:", self.__balance)

    @get_details.setter
    def set(self, details):
        self.__account_number, self.__balance = details


def main():
    bank = BankAccount("12345", 100.00)
    bank.get_details

    bank.deposit(50)
    bank.get_details

    bank.withdraw(30)
    bank.get_details

    bank.withdraw(150)
    bank.get_details

if __name__ == "__main__":
    main()