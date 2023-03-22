
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
                customers = create_cust()
            elif selection == 2:
                display_cust(customers)
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
    customer_list = {}
    while(True):
        try:
            numberOfCustomers = int(input('\nHow many customers would you like to create?: '))
            
            if numberOfCustomers <= 100:
                for customer in range(numberOfCustomers):
                    print(f'Creating customer #{customer+1}:')
                    cust_name = input('Please enter the name of the customer: ')
                    cust_id = random.randint(10000, 999999)
                    balance = random.randint(1000, 7500)
                    baseInterest = float(input('Please set the users interest rate: '))
                    highInterest = baseInterest + INTEREST_MODIFIER
                    cutoff = INTEREST_CUTOFF
                    account = BankAccount.BankAccount(cust_name, cust_id, baseInterest, highInterest, cutoff, balance)
                    customer_list.add(account)
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
    name = input("Please enter a new name for the customer (or 'ENTER' to skip): ")
    if name == "":
        print('Value not updated')
    else:
        account.setName(name)
        print('Customer updated.')
    base_interest = input("Please input the new BASE interest rate (or 'ENTER' to skip): ")
    if base_interest() == "":
        print('Value not updated')
    else:
        try:
            new_base_interest = float(input('Please enter the new interest rate: ')
            high_interest = new_base_interest + INTEREST_MODIFIER    
            account.setInterest(new_base_interest, high_interest)
            print('Customer updated.')
        except ValueError:
            print("Invalid input. Value not updated")
    balance = input("Please input the new balance (or 'ENTER' to skip): ")
    if balance() == "":
        print('Value not updated')
    else:
        try:
            new_balance = float(input('Please enter a new balacne: '))
            account.setBalance(new_balance)
            print('Customer updated.')
        except ValueError:
            print("Invalid input. Not updated")


def view_account():
    pass
    # parse list and view info specific to customer

main()
