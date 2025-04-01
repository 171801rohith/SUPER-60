
from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, price):
        pass


class StandardDiscount(DiscountStrategy):
    def calculate_discount(self, price):
        return price * 0.1


class NoDiscount(DiscountStrategy):
    def calculate_discount(self, price):
        return 0


class DiscountCalculator:
    def _init_(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy

    def calculate_discount(self, price):
        return self.discount_strategy.calculate_discount(price)


# Refactor the DiscountCalculator to follow OCP, so you can add new customer types (like "Premium" or "VIP") without changing the existing code.

from abc import ABC, abstractmethod


class Customer(ABC):
    @abstractmethod
    def get_discount(self, price):
        pass


class StandardCustomer(Customer):
    def get_discount(self, price):
        return price * 0.1  # 10% discount


class PremiumCustomer(Customer):
    def get_discount(self, price):
        return price * 0.2  # 20% discount


class VIPCustomer(Customer):
    def get_discount(self, price):
        return price * 0.3  # 30% discount


class SuperVIPCustomer(Customer):
    def get_discount(self, price):
        return price * 0.4  # 40% discount


class RegularCustomer(Customer):
    def get_discount(self, price):
        return 0  # No discount


class DiscountCalculator:
    def calculate_discount(self, customer: Customer, price):
        return customer.get_discount(price)


calculator = DiscountCalculator()

standard = StandardCustomer()
premium = PremiumCustomer()
vip = VIPCustomer()
regular = RegularCustomer()
superVip = SuperVIPCustomer()

print(calculator.calculate_discount(standard, 100))  # 10% discount
print(calculator.calculate_discount(premium, 100))  # 20% discount
print(calculator.calculate_discount(vip, 100))  # 30% discount
print(calculator.calculate_discount(regular, 100))  # No discount
print(calculator.calculate_discount(superVip, 100))


class PaymentProcessorType:
    def process_payment(self, method, amount):
        if method == "credit_card":
            print(f"Processing credit card payment of ${amount}")
            # Imagine credit card processing logic here
        elif method == "paypal":
            print(f"Processing PayPal payment of ${amount}")
            # Imagine PayPal processing logic here
        else:
            raise ValueError("Unsupported payment method")


class PaymentProcessorType(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCard(PaymentProcessorType):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")


class PayPal(PaymentProcessorType):
    def process_payment(self, amount):
        print(f"Processing Pay Pal payment of ${amount}")


class GooglePay(PaymentProcessorType):
    def process_payment(self, amount):
        print(f"Processing Google Pay payment of ${amount}")


class PaymentProcessor:
    def process_payment(self, method: PaymentProcessorType, amount):
        method.process_payment(amount)


creditCard = CreditCard()
payPal = PayPal()
googlePay = GooglePay()

paymentProcessor = PaymentProcessor()

paymentProcessor.process_payment(creditCard, 100)
paymentProcessor.process_payment(googlePay, 130)
paymentProcessor.process_payment(payPal, 100)