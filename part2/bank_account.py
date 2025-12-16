

class BankAccount:
      def __init__(self, account_number, holder_name,
         balance):
        self.account_number = account_number
        self.balance = balance
        self.holder_name=holder_name
      
      def deposit(self, amount):
        if amount < 0:
           return print("Invalid amount")
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}") 

      def withrdrawal(self, amount):
        if amount < 0:
           return print("Invalid amount")
        if amount > self.balance:
           return print("Insufficient funds")
        self.balance -= amount
        print(f"₹{amount} withdrawn. Remaining balance: ₹{self.balance}")

      def get_balance(self):
        print(f"Current balance: ₹{self.balance}")
        return self.balance
      
      def get_account_number(self):
        print
        return self.account_number
      
      def display_account(self):
        print("----- Bank Account Details -----")
        print(f"Account No: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: ₹{self.balance}")



acc1 = BankAccount(1001, "Medha", 5000)

acc1.deposit(2000)
acc1.withrdrawal(1500)
acc1.get_balance()
acc1.get_account_number()
acc1.display_account()    