import random
import BankAccountCopy

INTEREST_CUTOFF = 5000
INTEREST_MODIFIER = 1.5

def main():
    id = random.randint(100000, 999999)
    name = input('Please input customer name: ')
    interest = float(input('Please input the BASE interest rate: '))
    balance = float(input('Please input the starting balance: '))
    
    account = BankAccountCopy.BankAccount(name, id, interest, balance)

    deposit = float(input('Please input deposit: '))
    while deposit < 0:
        float(input('Please input a positive number: '))
    account.deposit(deposit)
    print(f'${deposit:.2f} deposited. New balance is '
    f'{account.getBalance():.2f}$')
    print()
    
    withdraw = float(input('Please input withdraw: '))
    while withdraw >= account.getBalance():
        withdraw = float(input('Insufficient funds! Input new number: '))
    account.withdraw(withdraw)
    print(f'{withdraw:.2f}$ withdrawn. New balance is '
    f'{account.getBalance():.2f}$')  
    print()

    balance = account.getBalance()
    if balance > INTEREST_CUTOFF:
        interest += INTEREST_MODIFIER
        account.setInterest(interest)
    else:
        account.setInterest(interest)
    
    print(f'{account.getBalance():.2f}')
    print(f'{account.getInterestRate():.2f}')
    print(f'{account.getMonthlyInterest():.2f}')
    print()
    
    print(str(account))

main()