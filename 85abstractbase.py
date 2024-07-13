from abc import ABC, abstractmethod

class bank(ABC):
    @abstractmethod
    def loan(self):pass
    
    @abstractmethod
    def credit(self):pass
    
class hdfc(bank):
    def loan(self):
        print("Hdfc bank provide loan for 8% interest")
        
    def credit(self):
        print("We provide the credit for bank")
        
    def card(self):
        print("provide credit card")
o=hdfc()
o.card()
o.loan()
o.credit()