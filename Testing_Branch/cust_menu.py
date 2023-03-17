# Customer-side menu

import BankAccountCopy as cust
import random

INTEREST_CUTOFF = 5000
INTEREST_MODIFIER = 1.5

# def cust_access():
#     customer = load_customers()
#     cust_id = input('Please enter your six-digit ID number: ')
#     if cust_id in customer:
#         cust_menu(cust_id)
#     else:
#         cust_id = input('ID not found! Please try again: ')

def main():
    id = random.randint(100000, 999999)
    name = input('Please input customer name: ')
    interest = float(input('Please input the BASE interest rate: '))
    balance = float(input('Please input the starting balance: '))
    account = cust.BankAccount(name, id, interest, balance)
    cust_menu(account)

def cust_menu(account):
    while True:
        try:
            print(f"\n{'Menu':^20}")
            print(f"{'-'*20}")
            print('1: Check Account Details')
            print('2: Withdraw Money')
            print('3: Deposit Money')
            print('4: Monthly Interest Rate')
            print('5: Monthly Interest Earned')
            print('6: Exit')
            selection = int(input('Please make your selection: '))

            if selection == 1:
                print(account)
            elif selection == 2:
                amount = float(input('Please enter the amount to withdraw: '))
                withdraw(account, amount)
            elif selection == 3:
                amount = float(input('Please enter the amount to deposit: '))
                deposit(account, amount)
            elif selection == 4:
                monthlyInterest(account)
            elif selection == 5:
                print('Your interest amount is '
                f'{account.getMonthlyInterest():.2f}$')
            elif selection == 6:
                 exit()
            else:
                print('Invalid number; please enter a '
                'number between 1-6!')
        except ValueError:
                print('Invalid input; please once again '
                'do not enter characters!')

def withdraw(account, withdraw):
    while withdraw >= account.getBalance():
        withdraw = float(input('Insufficient funds! Input new number: '))
    account.withdraw(withdraw)
    print(f'{withdraw:.2f}$ withdrawn. New balance is '
    f'{account.getBalance():.2f}$') 

def deposit(account, dep_amount):
    while dep_amount < 0:
        float(input('Please input a positive number: '))
    account.deposit(dep_amount)
    print(f'{dep_amount:.2f}$ deposited. New balance is '
    f'{account.getBalance():.2f}$')

def monthlyInterest(account):
    print(f'{interest:.2f}%')
    balance = account.getBalance()
    if balance > INTEREST_CUTOFF:
        interest += (INTEREST_MODIFIER / 100)
        account.setInterest(interest)
    else:
        account.setInterest(interest)
    print(f'{interest:.2f}%')

main()