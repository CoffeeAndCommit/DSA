#  Base account model 


import datetime


class BankAccount:
    def __init__(self, account_number,  holder_name , pin ,balanc=0 ):
        self.account_number = account_number
        self.holder_name = holder_name
        self.pin = pin
        self.balance = balanc

    def authenticate(self, pin):
        return self.pin == pin
    
    def deposit(self, amount):
        self.balance += amount
        self._add_transaction("DEPOSIT", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self._add_transaction("WITHDRAW", amount)

    def _add_transaction(self, txn_type, amount):
        self.transactions.append({
            "type": txn_type,
            "amount": amount,
            "time": datetime.now()
        })