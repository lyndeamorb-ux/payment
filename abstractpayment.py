from abc import ABC, abstractmethod

class Paymentamethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Paymentamethod):
    def pay(self, amount):
        print("Charging", amount, "to credit card")

class PayPal (Paymentamethod):
    def pay(self, amount):
         print("Sending", amount, "via PayPal")

class Gcash(Paymentamethod):
    def pay(self, amount):
        print("Sending", amount, "pay gcash")

methods = [CreditCard(), PayPal(), Gcash()]
for m in methods:
    m.pay(49.99)
        