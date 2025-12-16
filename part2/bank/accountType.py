#  defining account type using inhertiacee


from part2.bank_account import BankAccount


class SavinAccount(BankAccount):
    def __init__(self, account_number, holder_name, pin, balance =0):
        super().__init__(account_number, holder_name, pin, balance)
        self.interest_rate = 0.04

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self._add_transaction("INTEREST", interest)     
        return interest
    

class CurrentAccount(BankAccount):
    def __init__(self, account_no, holder_name, pin, balance=0):
        super().__init__(account_no, holder_name, pin, balance)
        self.overdraft_limit = 10000

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")
        self.balance -= amount
        self._add_transaction("WITHDRAW", amount)