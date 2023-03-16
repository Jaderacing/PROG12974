import BankAccount

account = BankAccount.BankAccount

def main():
    # Before the user is sent to the menu, they must enter a valid six-digit ID
    # If ID is not valid, continue to ask the user to enter a valid ID until one is inputted
    securityMeasure = 0 # A running total value for the security measure portion of the program 

    while True:
        
        try:
            
            customer_id = int(input('Please enter your six-digit ID: '))
            if len(str(customer_id)) == 6: # Checkes inputted int value by the user to ensure that it is 6 digits
                
                if customer_id == 346792: # User 1  
                        account = user1
                        menu(account) 
                elif customer_id == 923565: # User 2
                        account = user2
                        menu(account)
                elif customer_id == 156288: # User 3
                        account = user3
                        menu(account)
                elif customer_id == 997587: # User 4
                        account = user4
                        menu(account)
                elif customer_id == 987890: # User 5
                        account = user5
                        menu(account)
                else:
                    print("That is not a registered ID!\n")
                    securityMeasure += 1
                    
            else:
                    print('Please enter a valid six-digit ID!\n')
                    
            if securityMeasure == 3: # Locks the user out of the program after 3 failed attempts
                print('You have been locked out of the system! \nReason: Too many attempts. \nPlease try again later')
                break    

        except ValueError:
            print('Please do not enter characters!\n')

def menu(account):
    # Menu with error handling
    # Selections pass class, error handling changed to class
    # for cleaner code and functions in main()
    while True:
        try:
            print(f"\n{'Menu':^20}")
            print(f"{'-'*20}")
            print(f"{'1: Check Balance'}")
            print(f"{'2: Withdraw Money'}")
            print(f"{'3: Deposit Money'}")
            print(f"{'4: Monthly Interest Rate'}")
            print(f"{'5: Monthly Interest Earned'}")
            print(f"{'6: Exit'}")

            selection = int(input('Please make your selection: '))

            if selection == 1:
                print(f'Your balance for the account is ${account.getBalance():.2f}')
            
            elif selection == 2:
                withdraw = float(input('Please enter the amount that you would like to withdraw: '))
                account.withdraw(withdraw)
                print(f'Your new balance is ${account.getBalance():.2f}')

            elif selection == 3:
                deposit = float(input('Please input the amount that you would like to deposit: '))
                account.deposit(deposit)
                print(f'Your new balance is ${account.getBalance():.2f}')

            elif selection == 4:
                print(f'Your monthly interest rate is {account.getMonthlyInterestRate():.2f}%')

            elif selection == 5:
                print(f'Your balance for the account is ${account.getBalance():.2f}')
                print(f'Your interest amount is ${account.getMonthlyInterest():.2f}')

            elif selection == 6:
                 exit()
            else:
                print('Invalid number; please enter a number between 1-6!')
                
        except ValueError:
                print('Invalid input; please once again do not enter characters!')

# Call the main function when the program is run from this file
if __name__ == "__main__":
    main()