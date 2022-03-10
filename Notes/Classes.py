class Bank:

    def __init__(self, name='none'):
        self.balance = None
        self.name = name

    def set_bal(self, balance=0):
        self.balance = balance

