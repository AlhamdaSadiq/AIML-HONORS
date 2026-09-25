from abc import ABC
from abc import abstractmethod
from payment import RazorpayFactory, StripeFactory


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
        payment = RazorpayFactory.get_payment_object(method_type, **kwargs)
        return payment.pay(amount)


class StripeAggregator(Aggregator):
    def __init__(self):
        super().__init__("Stripe", 2.9)

    def call_get_payment_object(self, method_type, amount, **kwargs):
        payment = StripeFactory.get_payment_object(method_type, **kwargs)
        return payment.pay(amount)


class AggregatorFactory:

    factory = {
        "stripe": StripeAggregator,
        "razorpay": RazorpayAggregator }

    @classmethod
    def get_aggregator_object(cls, aggregator_name):
        if aggregator_name not in cls.factory:
            raise ValueError("Invalid aggregator")

        return cls.factory[aggregator_name]()

