class Payment:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}...")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}...")

class BitcoinPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Bitcoin payment of {amount}...")


credit_payment = CreditCardPayment()
paypal_payment = PayPalPayment()
bitcoin_payment = BitcoinPayment()

credit_payment.process_payment(100)
paypal_payment.process_payment(150)
bitcoin_payment.process_payment(200)
