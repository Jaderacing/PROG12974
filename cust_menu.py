# Customer-side menu

import BankAccountCopy

def cust_access():
    customer = load_customers()
    cust_id = input('Please enter your six-digit ID number: ')
    if cust_id in customer:
        cust_menu(cust_id)
    else:
        cust_id = input('ID not found! Please try again: ')

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
                with_amount = float(input('Please enter the amount that you '
                'would like to withdraw: '))
                withdraw(with_amount)
            elif selection == 3:
                dep_amount = float(input('Please input the amount that you would'
                ' like to deposit: '))
                deposit(dep_amount)
            elif selection == 4:
                print(f'Your monthly interest rate is '
                f'{account.getInterestRate():.2f}%')
            elif selection == 5:
                print('Your balance for the account is '
                f'${account.getBalance():.2f}')
                print('Your interest amount is '
                f'${account.getMonthlyInterest():.2f}')
            elif selection == 6:
                 exit()
            else:
                print('Invalid number; please enter a '
                'number between 1-6!')
        except ValueError:
                print('Invalid input; please once again '
                'do not enter characters!')

def withdraw(amount):
    while amount < 0:
        amount = float(input('Please input a positive number: '))
    account.withdraw(amount)
    print(f'Your new balance is ${account.getBalance():.2f}')

def deposit(amount):
    while amount < 0:
        amount = float(input('Please input a positive number: '))
    account.deposit(amount)
    print(f'Your new balance is ${account.getBalance():.2f}')