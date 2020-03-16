import sys


class Bank:
    logged_in = False
    balance = 0

    def __init__(self, username, password, fname, lname):
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname

    def verify_login(self, user_dict):
        for key, value in user_dict.items():
            if self.username == key and self.password == value:
                self.logged_in = True
        if not self.logged_in:
            sys.exit("Invalid Credentials")
        else:
            print(f'Welcome {self.fname} {self.lname}')

    def deposit_money(self, amount):
        self.balance += amount

    def withdraw_money(self, amount, type):
        if self.balance > amount:
            self.balance -= amount
            print(f'Rs {amount} withdrawn from your account. Remaining account balance is {self.balance}')
        else:
            print(f'Maximum amount withdrawable is {self.balance}')


class Savings(Bank):
    saving_user_dict = {'KEDAR': 'radek@30', 'RADEK': 'radek@30'}
    daily_withdrawable_limit = 10000
    total_transactions = []

    def __init__(self, username, password, fname, lname):
        super().__init__(username, password, fname, lname)
        self.verify_login(self.saving_user_dict)


s1 = Savings('KEDAR', 'radek@30', 'Kedar', 'Navare', 'Savings')
s1.deposit_money(10000)
s1.withdraw_money(5000)
s1.withdraw_money(6000)
