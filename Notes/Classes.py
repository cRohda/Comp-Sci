class Bank:

    def __init__(self, name='none'):
        self.balance = None
        self.name = name

    def set_bal(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return self.balance
        else:
            self.balance -= amount
            return self.balance
