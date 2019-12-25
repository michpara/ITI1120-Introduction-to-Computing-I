class BankAccount:
    'class that represents a bank account'

    def __init__(self, balance = 0):
        '''(Point, Nmber) -> None'''
        self.balance = balance

    def withdraw(self, amount):
        '''(Point, number)-> None
        withdraws amount from balance'''
        self.balance -= amount

    def deposit(self, amount):
        '''(Point, number)->None
        deposits amount into balance'''
        self.balance += amount

    def getBalance(self):
        '''(Point)->Number
        returns the bank balance'''
        return self.balance

    def __repr__(self):
        '''(Point)->String
        return formal representation'''
        return 'BankAccount(' + str(self.balance) + ')'
