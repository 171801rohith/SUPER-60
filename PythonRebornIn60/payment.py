# Exercise 3: Polymorphism with Payment Processing
# Objective: Process different payment methods polymorphically.

# Instructions:
# Create a base class Payment with a method process(self, amount) that raises a NotImplementedError.
# Create three derived classes:
# CreditCard that overrides process(self, amount) to print "Processing credit card payment of <amount>."
# PayPal that overrides process(self, amount) to print "Processing PayPal payment of <amount>."
# BankTransfer that overrides process(self, amount) to print "Processing bank transfer of <amount>."
# Write a function make_payment(payment, amount) that takes a Payment object and an amount, then calls process(amount).
# In main(), create a list of payments (one of each type), and use a loop to call make_payment() with an amount of 100 for each.


class Payment:
    def process(self, amount):
        raise NotImplementedError


class CreditCard(Payment):
    def process(self, amount):
        print(f"Processing CreditCard payment of {amount}")


class PayPal(Payment):
    def process(self, amount):
        print(f"Processing PayPal payment of {amount}")


class BankTransfer(Payment):
    def process(self, amount):
        print(f"Processing BankTransfer payment of {amount}")


def make_payment(payment, amount):
    payment.process(amount)


def main():
    payments = [CreditCard(), PayPal(), BankTransfer()]

    for payment in payments:
        make_payment(payment, 100)


if __name__ == "__main__":
    main()
