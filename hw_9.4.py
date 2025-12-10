class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

class SavingsAccount(Account):
    def add_interest(self):
        rate = 0.05
        interest_amount = self.balance * rate
        self.balance += interest_amount

account = SavingsAccount(1000)
account.deposit(500)
account.add_interest()
print(account.balance)