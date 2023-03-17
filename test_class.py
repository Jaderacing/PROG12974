import random
import BankAccountCopy

INTEREST_CUTOFF = 5000

def main():
    id = random.randint(100000, 999999)
    name = input('Please input customer name: ')
    interest = float(input('Please input the BASE interest rate: '))
    interestHigh = float(input('Please input the higher interest rate: '))
    balance = float(input('Please input the starting balance: '))
    if balance > INTEREST_CUTOFF:
        interest = interestHigh
    
    account = BankAccountCopy.BankAccount(name, id, interest, balance)

    deposit = float(input('Please input deposit: '))
    withdraw = float(input('Please input withdraw: '))
    account.deposit(deposit)
    print(f'{account.getBalance():.2f}')
    account.withdraw(withdraw)
    print(f'{account.getBalance():.2f}')
    print(f'{account.getInterestRate():.2f}')
    print(f'{account.getMonthlyInterest():.2f}')
    print()
    print(str(account))

main()