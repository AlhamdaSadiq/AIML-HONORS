from abc import ABC
from abc import abstractmethod
from typing import Dict
from typing import Type


class PayementMethod(ABC):

    @abstractmethod
    def get_details(self)-> str:
        pass

    @abstractmethod
    def pay(self,amount:float)-> bool:
        pass


class RazorpayCardPayment(PaymentMethod):
    def __init__(self,card_number):
        self.card_number = card_number

    def get_details(self):
        return f"Razorpay Card : {self.card_number}"

    def pay(self,amount):
        print(f"Razorpay Card Payment of Rs. {amount} successful!")
        return True


class RazorpayUPIPayment(PaymentMethod):
    def __init__(self,upi_number):
        self.upi_number = upi_number

    def get_details(self):
        return  f"Razorpay UPI : {self.upi_number}"

    def pay(self,amount):
        print(f"Razorpay UPI Payment of Rs. {amount} successfull!")
        return True




class StripeCardPayment(PaymentMethod):
    def __init__(self,card_number):
        self.card_number = card_number

    def get_details(self):
        return f"Stripe Card : {self.card_number}"

    def pay(self,amount):
        print(f"Stripe Card Payment of Rs. {amount} successful!")
        return True


class StripeUPIPayment(PaymentMethod):
    def __init__(self,upi_number):
        self.upi_number = upi_number

    def get_details(self):
        return  f"Stripe UPI : {self.upi_number}"

    def pay(self,amount):
        print(f"Stripe UPI Payment of Rs. {amount} successfull!")
        return True



class FactoryPaymentMethod(ABC):

    factory: Dict[str, Type[PaymentMethod]] = {}

    @classmethod
    def get_payment_object(cls, method_type: str, **kwargs) -> PaymentMethod:
        if method_type not in cls.factory:
            raise ValueError("Invalid payment method")
        return cls.factory[method_type](**kwargs)


class RazorpayFactory(FactoryPaymentMethod):
    factory = {
        "card": RazorpayCardPayment,
        "upi": RazorpayUPIPayment }


class StripeFactory(FactoryPaymentMethod):
    factory = {
        "card": StripeCardPayment,
        "upi": StripeUPIPayment }
