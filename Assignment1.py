from abc import ABC, abstractmethod
from typing import Dict, Type

class PaymentMethod(ABC):

    @abstractmethod
    def get_details(self) -> str:
        pass

    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class RazorpayCardPayment(PaymentMethod):

    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return f"Razorpay Card: {self.card_number}"

    def pay(self, amount):
        print(f"Razorpay Card Payment of Rs. {amount} successful!")
        return True

class RazorpayUPIPayment(PaymentMethod):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return f"Razorpay UPI: {self.upi_id}"

    def pay(self, amount):
        print(f"Razorpay UPI Payment of Rs. {amount} successful!")
        return True
      
class StripeCardPayment(PaymentMethod):

    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return f"Stripe Card: {self.card_number}"

    def pay(self, amount):
        print(f"Stripe Card Payment of Rs. {amount} successful!")
        return True

class StripeUPIPayment(PaymentMethod):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return f"Stripe UPI: {self.upi_id}"

    def pay(self, amount):
        print(f"Stripe UPI Payment of Rs. {amount} successful!")
        return True

class FactoryPaymentMethod(ABC):

    factory: Dict[str, Type[PaymentMethod]] = {}

    @classmethod
    def get_payment_object(cls, method_type, **kwargs):

        if method_type not in cls.factory:
            raise ValueError("Invalid payment method")

        return cls.factory[method_type](**kwargs)

class RazorpayFactory(FactoryPaymentMethod):

    factory = {
        "card": RazorpayCardPayment,
        "upi": RazorpayUPIPayment
    }

class StripeFactory(FactoryPaymentMethod):

    factory = {
        "card": StripeCardPayment,
        "upi": StripeUPIPayment
    }

class Aggregator(ABC):

    def __init__(self, name, processing_fee):
        self.name = name
        self.processing_fee = processing_fee

    @abstractmethod
    def call_get_payment_object(self, method_type, amount, **kwargs):
        pass

class RazorpayAggregator(Aggregator):

    def __init__(self):
        super().__init__("Razorpay", 2.0)

    def call_get_payment_object(self, method_type, amount, **kwargs):

        payment = RazorpayFactory.get_payment_object(
            method_type, **kwargs
        )

        return payment.pay(amount)

class StripeAggregator(Aggregator):

    def __init__(self):
        super().__init__("Stripe", 2.9)

    def call_get_payment_object(self, method_type, amount, **kwargs):

        payment = StripeFactory.get_payment_object(
            method_type, **kwargs
        )

        return payment.pay(amount)

class AggregatorFactory:

    factory = {
        "stripe": StripeAggregator,
        "razorpay": RazorpayAggregator
    }

    @classmethod
    def get_aggregator_object(cls, aggregator_name):

        if aggregator_name not in cls.factory:
            raise ValueError("Invalid aggregator")

        return cls.factory[aggregator_name]()

def main():

    try:

        aggregator_name = input(
            "Enter aggregator (Stripe/Razorpay): "
        ).lower()

        method_type = input(
            "Enter method (Card/UPI): "
        ).lower()

        if method_type == "card":

            details = input("Enter card number: ")
            kwargs = {"card_number": details}

        elif method_type == "upi":

            details = input("Enter UPI ID: ")
            kwargs = {"upi_id": details}

        else:
            raise ValueError("Invalid payment method")

        amount = float(input("Enter amount: "))

        if amount <= 0:
            raise ValueError("Amount must be positive")

        aggregator = AggregatorFactory.get_aggregator_object(
            aggregator_name
        )

        result = aggregator.call_get_payment_object(
            method_type, amount, **kwargs
        )

        if result:
            print("Payment completed successfully!")

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
