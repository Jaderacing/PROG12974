# Menu for selecting which user branch to use
# Date v1.0 2023-03-16

import BankAccount
import random
INTEREST_CUTOFF = 5000 # Amount in which the higher interest applies
INTEREST_MODIFIER = 1.5 # Amount to ADD to the base interest rate

def main():
    while True:
        try:
            print(f"\n{'Menu':^20}")
            print(f"{'-'*20}")
            print("""Which system would you like to access:
            1: Administrator
            2: Customer
            3: Exit""")
            selection = int(input('Please make your selection: '))

            if selection == 1:
                admin_menu()
            elif selection == 2:
                cust_input()
            else:
                exit()
        except ValueError:
            print('Invalid input; please once again do not enter characters!')

# Administrative menu
def admin_menu():
    pass
    while True:
        try:
            print(f"\n{'Menu':^20}")
            print(f"{'-'*20}")
            print("""Which system would you like to access:
1: Create Customer(s)
2: Display Customers
3: View Customer Account
4: Update Customer Account
5: Exit""")
            selection = int(input('Please make your selection: '))

            if selection == 1:
                create_cust()
            elif selection == 2:
                display_cust()
                # print account list
            elif selection == 3:
                pass
                view_account()
            elif selection == 4:
                pass
                update_cust()
            elif selection == 5:
                exit()
            else:
                selection = int(input('Please input a number between 1-5: '))
        except ValueError:
            print('Invalid input; please once again do not enter characters!')

def create_cust():
    customer_list = []
    while(True):
        try:
            numberOfCustomers = int(input('\nHow many customers would you like to create?: '))
            
            if numberOfCustomers <= 100:
                for customer in range(numberOfCustomers):
                    print(f'Creating customer #{customer+1}:')
                    cust_name = input('Please enter the name of the customer: ')
                    cust_id = random.randint(10000, 999999)
                    balance = random.randint(1000, 5000)
                    baseInterest = float(input('Please set the users interest rate: '))
                    highInterest = baseInterest + INTEREST_MODIFIER
                    cutoff = INTEREST_CUTOFF
                    account = BankAccount.BankAccount(cust_name, cust_id, baseInterest, highInterest, cutoff, balance)
                    customer_list.append(account)
                print(f'{numberOfCustomers} new customers have been created.')
            else:
                print('Please create no more than 100 new customers!')
                continue  
        except ValueError:
            print('Invalid input; please try again!')
            continue

        return customer_list
    


def display_cust(customer_list):
    i = 1
    for cust in customer_list:
        print(f'Customer {i}: {cust}')
        i += 1
        
def update_cust():
    pass
    # parse customer list and update info
    name = input('Please enter a new name for the customer: ')
    base_interest = float(input('Please input the new BASE interest rate: '))
    high_interest = base_interest + INTEREST_MODIFIER
    balance = float(input('Please input the new balance: '))
    BankAccount.setName(name)
    BankAccount.setBalance(balance)
    BankAccount.setInterest(base_interest, high_interest)

def view_account():
    pass
    # parse list and view info specific to customer

def cust_input():
    id = int(input('Please input your six-digit ID: '))
    # Parse list for ID and send to BankAccount.BankAccout()
    account = BankAccount.BankAccount()
    cust_menu(account)

# THIS BLOCK FOR TESTING ONLY
###########################################################################
import BankAccount as cust
import random

INTEREST_MODIFIER = 1.5
INTEREST_CUTOFF = 5000

def main():
    id = random.randint(100000, 999999)
    name = input('Please input customer name: ')
    interest = float(input('Please input the BASE interest rate: '))
    highInterest = interest + INTEREST_MODIFIER
    cutoff = INTEREST_CUTOFF
    balance = float(input('Please input the starting balance: '))
    account = cust.BankAccount(name, id, interest, highInterest, cutoff, balance)
    cust_menu(account)
###########################################################################

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
                print(f'{account.getInterestRate():.2f}%')
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
    print(f'{account.getMonthlyInterest():.2f}$')

main()