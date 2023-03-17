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
        
    def setHighInterst(self, highInterest):
        if self.__balance > 5000:
            self.__interestRate = highInterest
        return self.__interestRate
    
# Methods
# Allows the user to withdraw an amount of money from their account
    def withdraw(self, amount): 
        try:
            while amount > self.__balance:
                amount = float(input("""Error; insufficient funds!
Please input a new value: """))
            print(f'${amount} withdrawn.')
        except ValueError:
            amount = float(input('Invalid characters. Please input '
            'a number: '))

# Allows the user to deposit an amount of money into their account
    def deposit(self, amount):
        try:
            while amount <= 0:
                amount = float(input('Invalid number. Please input '
                'positive number: '))
            print(f'${amount:.2f} deposited.')
            self.__balance += amount
        except ValueError:
            amount = float(input('Invalid characters. Please input '
            'a valid number: '))

# Calculates interest amount accumulated on a period of time
    def getMonthlyInterest(self):
        try:
            duration = int(input('For how many months would you like '
            'to calculate the interest? '))
            for count in range(duration):
                interest = (self.__interestRate / 12 / 100) * self.__balance
                self.__interestAmount += interest
        except ValueError:
            duration = int(input('Please input a valid number: '))
        return self.__interestAmount

# Accessors
    def getBalance(self):
        return self.__balance

    def getInterestRate(self):
        return float(self.__interestRate / 12)
