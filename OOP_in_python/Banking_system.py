class InsufficientFunds(Exception):
    pass

class BankAccount :
    def __init__(self,holdername,blc):
        self.name=holdername
        self.balance=blc

    def withdrawal(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withdrew ₹{amount}. Current balance: ₹{self.balance}")

        else:
            raise InsufficientFunds("This amount is not available")
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"deposit {amount}\ncurrent Balance {self.balance}")
            
        else: print('something went wrong')
    def display(self):
        print(f"Name {self.name}")
        print(f"balance={self.balance}")


a = BankAccount("aakash",1000)
a.deposit(100000)
a.withdrawal(546)
a.display()
