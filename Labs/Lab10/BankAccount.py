class BankAccount:
    'class that represents a bank account'

    def __init__(self, balance = 0):
        '''(BankAccount, Nmber) -> None'''
        self.balance = balance

    def withdraw(self, amount):
        '''(BankAccount, number)-> None
        withdraws amount from balance'''
        self.balance -= amount

    def deposit(self, amount):
        '''(BankAccount, number)->None
        deposits amount into balance'''
        self.balance += amount

    def getBalance(self):
        '''(BankAccount)->Number
        returns the bank balance'''
        return self.balance

    def __repr__(self):
        '''(BankAccount)->String
        return formal representation'''
        return 'BankAccount(' + str(self.balance) + ')'
