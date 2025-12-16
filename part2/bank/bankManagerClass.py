class BankManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc):
        self.accounts[acc.account_no] = acc

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)
