# Menu for selecting which user branch to use
# Date v1.0 2023-03-16

import BankAccount
import random
import pickle

INTEREST_CUTOFF = 5000 # Amount in which the higher interest applies
INTEREST_MODIFIER = 1.5 # Amount to ADD to the base interest rate
FILE = 'customers.dat'

def main():
    account = load_customers()
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
                customer_list = admin_menu()
                save_customers(customer_list)
            elif selection == 2:
                cust_input(account)
                #cust_menu(accounts)
            else:
                exit()
        except ValueError:
            print('Invalid input; please once again do not enter characters!')

# Administrative menu
def admin_menu():
    accounts = load_customers
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
                display_cust_list(accounts)
                # print account list
            elif selection == 3:
                view_cust(accounts)
            elif selection == 4:
                update_cust(accounts)
            elif selection == 5:
                return
            else:
                selection = int(input('Please input a number between 1-5: '))
        except ValueError:
            print('Invalid input; please once again do not enter characters!')

def create_cust():
    customer_list = {}
    while(True):
        try:
            numberOfCustomers = int(input('\nHow many customers would you like to create?: '))
            baseInterest = float(input('Please set the BASE interest rate: '))
            if numberOfCustomers >= 10 and numberOfCustomers <= 100:
                for customer in range(numberOfCustomers):
                    cust_id = random.randint(100000, 999999)
                    print(f"""Creating customer #{customer+1}
ID: {cust_id}: """)
                    cust_name = input('Please enter the name of the customer: ')
                    balance = int(input('Please input the starting balance: '))
                    highInterest = baseInterest + INTEREST_MODIFIER
                    account = BankAccount.BankAccount(cust_name, cust_id, baseInterest, highInterest, INTEREST_CUTOFF, balance)
                    customer_list[cust_id] = account
                print(f'File has been created with: {numberOfCustomers} new customers.')
                break
            else:
                print('Please create no less than 10, and no more than 100 customers!')
                continue  
        except ValueError:
            print('Invalid input; please try again!')
        save_customers(customer_list)
        return customer_list

# Load a dct or create one if not found
def load_customers():
    try:
        input_file = open(FILE, "rb")
        cust_dct = pickle.load(input_file)
        input_file.close() 
    except IOError:
        cust_dct = {}
    print(cust_dct)
    return cust_dct

def display_cust_list(list):
    list = load_customers()
    for key in list:
        print(key, list[key])
    # end_of_file = False
    # input_file = open(FILE, 'rb')
    # cust_dict = {}
    # while not end_of_file:
    #     try:
    #         cust = pickle.load(input_file)
    #         cust_dict[cust.self.__id()] = cust
    #         print(f'Name is {cust.self.__name()}\n')
    #         print(f'Name is {cust.self.__id()}\n')
    #         print(f'Name is {cust.self.__balance()}\n')
    #         print(f'Name is {cust.self.__interestRate()}\n')

    #     except EOFError:
    #         end_of_file = True
    # input_file.close()

# Update account information        
def update_cust(account):
    id = input('Please enter the ID to update: ')
    if id in account:
        name = input('Please enter a new name for the customer: ')
        try:
            new_base_interest = float(input('Please enter the new interest rate: '))
            high_interest = new_base_interest + INTEREST_MODIFIER
            print('Customer updated.')
        except ValueError:
            print("Invalid input. Value not updated")
        try:
            new_balance = float(input('Please enter a new balacne: '))
            print('Customer updated.')
        except ValueError:
            print("Invalid input. Not updated")
        update = BankAccount.BankAccount(name, id, new_base_interest, high_interest, INTEREST_CUTOFF, new_balance)
        account[id] = update
    else:
        print('Customer not found')
    save_customers(account)

def view_cust(account):
    id = int(input('Please input the ID of the customer: '))
    print(account.get(id, 'Customer not found'))
    return

def save_customers(customers):
    output_file=open(FILE, "wb")
    pickle.dump(customers, output_file)
    output_file.close()

def cust_input(account):
    id = int(input('Please input your six-digit ID or 0 to quit: '))
    if id in account:
        cust_menu(id)


# THIS BLOCK FOR TESTING ONLY
###########################################################################
###########################################################################
# import BankAccount as cust
# import random

# INTEREST_MODIFIER = 1.5
# INTEREST_CUTOFF = 5000

# def main():
#     id = random.randint(100000, 999999)
#     name = input('Please input customer name: ')
#     interest = float(input('Please input the BASE interest rate: '))
#     highInterest = interest + INTEREST_MODIFIER
#     cutoff = INTEREST_CUTOFF
#     balance = float(input('Please input the starting balance: '))
#     account = cust.BankAccount(name, id, interest, highInterest, cutoff, balance)
#     cust_menu(account)
###########################################################################
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
    while withdraw > account.getBalance():
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

if __name__ == '__main__':
    main()