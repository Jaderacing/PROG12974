# Class handling customer ID, name, balance, interest rate
# Withdraw and deposit handling
# Date: v1.0 2023-03-16

class BankAccount:
    def __init__(self, name, id, interest, balance):
        self.__id = id
        self.__name = name
        self.__balance = balance
        self.__interestRate = interest
        self.__interestAmount = 0

    def __str__(self):
        return f"""Customer Name: {self.__name}
Customer ID: {self.__id}
Customer Balance: ${self.__balance}
Customer Interest Rate: {self.__interestRate}%"""
    
# Mutators

    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name

    def setBalance(self, balance):
        self.__balance = balance

    def setInterest(self, interest):
        self.__interestRate = interest

    # def setHighInterest(self, highInterest):
    #     self.__highInterest = highInterest
    
# Methods
# Allows the user to withdraw an amount of money from their account
    def withdraw(self, amount):
        self.__balance -= amount 
        return self.__balance

# Allows the user to deposit an amount of money into their account
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

# Calculates interest amount accumulated on a period of time
    def getMonthlyInterest(self):
        duration = int(input('Input the time you would like to calculate the interest: '))
        self.__interestAmount = duration * ((self.__interestRate / 100 / 12) \
        * self.__balance)
        return self.__interestAmount

# Accessors
    def getBalance(self):
        return self.__balance

    def getInterestRate(self):
        return self.__interestRate / 12