# Class handling customer ID, name, balance, interest rate
# Withdraw and deposit handling
# Date: v1.0 2023-03-16

class BankAccount:
    def __init__(self, name, id, baseInterest, highInterest, cutoff, balance):
        self.__id = id
        self.__name = name
        self.__interestRate = baseInterest
        self.__baseInterest = baseInterest
        self.__highInterest = highInterest
        self.__balance = balance
        self.__cutoff = cutoff
        self.__interestAmount = 0

    def __str__(self):
        return f"""Customer Name: {self.__name}
Customer ID: {self.__id}
Customer Balance: ${self.__balance}
Customer Interest Rate: {self.__interestRate}%"""
    
# Mutators
    def setName(self, name):
        self.__name = name

    def setBalance(self, balance):
        self.__balance = balance

    def setInterest(self, baseInterest, highInterest):
        self.__baseInterest = baseInterest
        self.__highInterest = highInterest
        if self.__balance > self.__cutoff:
            self.__interestRate = self.__highInterest
        else:
            self.__interestRate = self.__baseInterest
    
# Methods
# Allows the user to withdraw an amount of money from their account
    def withdraw(self, amount):
        self.__balance -= amount
        if self.__balance > self.__cutoff:
            self.__interestRate = self.__highInterest
        else:
            self.__interestRate = self.__baseInterest
        return self.__balance

# Allows the user to deposit an amount of money into their account
    def deposit(self, amount):
        self.__balance += amount
        if self.__balance > self.__cutoff:
            self.__interestRate = self.__highInterest
        else:
            self.__interestRate = self.__baseInterest
        return self.__balance

# Calculates interest amount accumulated on a period of time
    def getMonthlyInterest(self):
        duration = int(input('Input the time you would like to calculate the interest: '))        
        self.__interestAmount = duration * ((self.__interestRate / 100 / 12) * self.__balance)
        return self.__interestAmount

# Accessors
    def getBalance(self):
        return self.__balance

    def getInterestRate(self):
        return self.__interestRate / 12
    
    def getName(self):
        return self.__name