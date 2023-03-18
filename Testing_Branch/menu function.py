# Menu for selecting which user branch to use
# Date v1.0 2023-03-16

import BankAccount
import random

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
                cust_menu()
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
                    interest_rate = float(input('Please set the users interest rate: '))
                    account = BankAccount.BankAccount(cust_name, cust_id, interest_rate, balance)
                    customer_list.append(account)
                print(f'{numberOfCustomers} new customers have been created.')
            else:
                print('Please create no more than 100 new customers!')
                continue  
        except ValueError:
            print('Invalid input; please try again!')
            continue

        return customer_list
    
        # number of accounts to create ( <101 )
        # cust_name = 
        # cust id = random.randint(10000, 999999)
        # balance = 
        # interest_rate = 
        # higher interest rate = 
        # send higher interest rate to account.setHighInterest()
        # account.Backaccount(name, id, balance, interest_rate)

def display_cust(customer_list):
    i = 1
    for cust in customer_list:
        print(f'Customer {i}: {cust}')
        i += 1
        
def update_cust():
    pass
    # parse customer list and update info

def view_account():
    pass
    # parse list and view info specific to customer

# Customer-side menu
def cust_menu(account):
    pass
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
                f'{account.getMonthlyInterestRate():.2f}%')
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

if __name__ == '__main__':
    main()
