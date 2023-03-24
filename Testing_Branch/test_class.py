import BankAccount
import random
import pickle

INTEREST_MODIFIER = 1
INTEREST_CUTOFF = 5000
FILE = 'customers.dat'


def main():
    list = load_customers()
#    list = create_cust()
    for key in list:
        print(key, list[key])
        print(key)
    view_cust(list)
    save_customers(list)

def create_cust():
    customer_list = {}
    while(True):
        try:
            numberOfCustomers = int(input('\nHow many customers would you like to create?: '))
            if numberOfCustomers <= 100:
                for customer in range(numberOfCustomers):
                    print(f'Creating customer #{customer+1}:')
                    cust_name = 'Dave' #input('Please enter the name of the customer: ')
                    cust_id = random.randint(100000, 999999)
                    balance = random.randint(1000, 7500)
                    baseInterest = 3 #float(input('Please set the users interest rate: '))
                    highInterest = baseInterest + INTEREST_MODIFIER
                    cutoff = INTEREST_CUTOFF
                    account = BankAccount.BankAccount(cust_name, cust_id, baseInterest, highInterest, cutoff, balance)
                    customer_list[cust_id] = account
                print(f'{numberOfCustomers} new customers have been created.')
            else:
                print('Please create no more than 100 new customers!')
                continue  
        except ValueError:
            print('Invalid input; please try again!')
            continue
        return customer_list

def view_cust(account):
    id = int(input('Please input the id of the customer: '))
    print(account.get(id, 'Customer not found'))

def load_customers():
    try:
        input_file = open(FILE, "rb")
        cust_dct = pickle.load(input_file)
        input_file.close() 
    except IOError:
        cust_dct = {}
    return cust_dct

def save_customers(account):
    out_file = open(FILE, 'wb')
    pickle.dump(account, out_file)
    out_file.close()

def cust_input(account):
    id = int(input('Please input your six-digit ID: '))
    customer = account.get(id, 'User not found!')
    cust_menu(customer)

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