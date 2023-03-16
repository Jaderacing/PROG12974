# Menu for selecting which user branch to use
def main_menu():
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
    create_cust
    view_cust
    update_cust
    display_cust

# Customer-side menu
def cust_menu(account):
    pass
    while True:
        try:
            print(f"\n{'Menu':^20}")
            print(f"{'-'*20}")
            print('1: Account Details')
            print('2: Withdraw Money')
            print('3: Deposit Money')
            print('4: Monthly Interest Rate')
            print('5: Monthly Interest Earned')
            print('6: Exit')
            selection = int(input('Please make your selection: '))

            if selection == 1:
                print(f'Your balance for the account is '
                f'${account.getBalance():.2f}')
            elif selection == 2:
                withdraw = float(input('Please enter the amount that you '
                'would like to withdraw: '))
                account.withdraw(withdraw)
                print(f'Your new balance is ${account.getBalance():.2f}')
            elif selection == 3:
                deposit = float(input('Please input the amount that you would' ' like to deposit: '))
                account.deposit(deposit)
                print(f'Your new balance is ${account.getBalance():.2f}')
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