import pickle
import BankAccount
import random

INTEREST_CUTOFF = 5000 # Amount in which the higher interest applies
INTEREST_MODIFIER = 1.5 # Amount to ADD to the base interest rate

FILE = 'customers.dat'

def main():
    customers = load_customers()
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
                cust_input(customers)
            else:
                exit()
        except ValueError:
            print('Invalid input; please once again do not enter characters!')

# Administrative menu
def admin_menu():
    pass
    customers = load_customers()
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
                customer_list = create_cust()
                save_customers(customer_list)
            elif selection == 2:
                display_cust(customers)
            elif selection == 3:
                pass
                view_account(customers)
            elif selection == 4:
                pass
                update_cust(customers)
            elif selection == 5:
                exit()
            else:
                selection = int(input('Please input a number between 1-5: '))
        except ValueError:
            print('Invalid input; please once again do not enter characters!')

def create_cust():
    output_file = file.open(FILE, 'wb')
    customer_list = []
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
                    customer_list.append(account)
                print(f'{numberOfCustomers} new customers have been created.')
            else:
                print('Please create no more than 100 new customers!')
                continue  
        except ValueError:
            print('Invalid input; please try again!')
            continue
        finally:
            pickle.dump(account, output_file)
            output_file.close()
            print("The data was written to", FILE)
        return customer_list

def display_cust(customer_list):
    i = 1
    for cust in customer_list:
        print(f'Customer {i}: {cust}')
        i += 1
        
def update_cust():
    pass
    # parse customer list and update info
    name = input("Please enter a new name for the customer (or 'ENTER' to skip): ")
    if name.strip() == "":
        print('Value not updated')
    else:
        account.setName(name)
        print('Customer updated.')
    base_interest = input("Please input the new BASE interest rate (or 'ENTER' to skip): ")
    if base_interest.strip() == "":
        print('Value not updated')
    else:
        try:
            new_base_interest = float(base_interest)
            high_interest = new_base_interest + INTEREST_MODIFIER    
            account.setInterest(new_base_interest, high_interest)
            print('Customer updated.')
        except ValueError:
            print("Invalid input. Value not updated")
    balance = input("Please input the new balance (or 'ENTER' to skip): ")
    if balance.strip() == "":
        print('Value not updated')
    else:
        try:
            new_balance = float(balance)
            account.setBalance(new_balance)
            print('Customer updated.')
        except ValueError:
            print("Invalid input. Not updated")

def view_account(customer):
    name = input("Enter a name: ")
    print(customer.get(name, "That name is not found."))

def load_customers():
    try:
        input_file = open(FILE, "rb")
        cust_dct = pickle.load(input_file)
        input_file.close()
        
    except IOError:
        cust_dct = {}
        
    return cust_dct

def look_up(customer):
    name = input("Enter a name: ")
    print(customer.get(name, "That name is not found."))

def change(account):
    id = int(input("Enter an ID: "))
    if id in account:
        name = input("Please enter a new name for the customer (or 'ENTER' to skip): ")
        if name.strip() == "":
            print('Value not updated')
        else:
            account.setName(name)
            print('Customer updated.')
        base_interest = input("Please input the new BASE interest rate (or 'ENTER' to skip): ")
        if base_interest.strip() == "":
            print('Value not updated')
        else:
            try:
                new_base_interest = float(base_interest)
                high_interest = new_base_interest + INTEREST_MODIFIER    
                account.setInterest(new_base_interest, high_interest)
                print('Customer updated.')
            except ValueError:
                print("Invalid input. Value not updated")
        balance = input("Please input the new balance (or 'ENTER' to skip): ")
        if balance.strip() == "":
            print('Value not updated')
        else:
            try:
                new_balance = float(balance)
                account.setBalance(new_balance)
                print('Customer updated.')
            except ValueError:
                print("Invalid input. Not updated")
                account[name] = update
    else:
        print("That name is not found.")

def save_customers(customers):
    output_file=open(FILE, "wb")
    pickle.dump(customers, output_file)
    output_file.close()

def cust_input(id):
    id = input("Enter your id: ")
    print(id.get(name, "That name is not found."))
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

main()