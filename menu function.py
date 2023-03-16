# Menu for selecting which user branch to use
# Date v1.0 2023-03-16

import BankAccount
account = BankAccount.BankAccount()

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
                pass
                create_cust()
            elif selection == 2:
                pass
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
    pass
    account = BanckAccount.BankAccount()
        # number of accounts to create ( <101 )
        # cust_name = 
        # cust id = random.randint(10000, 999999)
        # balance = 
        # interest_rate = 
        # higher interest rate = 
        # send higher interest rate to account.setHighInterest()
        # account.Backaccount(name, id, balance, interest_rate)

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
