import BankAccount

# FILE = customers.dat

INTEREST_CUTOFF = 5000 # Amount in which the higher interest applies
INTEREST_MODIFIER = 1.5 # Amount to ADD to the base interest rate

# Administrative menu
def admin_menu():
    pass
    customer = load_customers()
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
                show_accounts()
            elif selection == 3:
                pass
                view_account(customer)
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
        # high interest rate = 
        # send higher interest rate to account.setHighInterest()
        # account.Backaccount(name, id, balance, interest_rate)

def show_accounts():
    pass
    cust_list = load_customers()
    print(cust_list)


def update_cust():
    pass
    customers = load_customers()
    change(customers)
    save_customers(customers)

def load_customers():
    try:
        input_file = open(FILE, 'rb')
        cust_list = pickle.load(input_file)
        input_file.close()
    except IOError:
        cust_list={}
    return cust_list

def change(customer):
    id = input("What is the ID of the customer you would like to change: ")
        # name = input('Enter the new name: ')
        # balance = float(input('Enter the new balance: '))
        # interest = input('Enter the new interest rate: ')
        # entry = account.BankAccount(name, balance, interest)
        # customer[name] = entry
        # print('Information updated.')
    # else:
    #     print('ID not found.')

def save_customers(customer):
    output_file=open(FILE, 'wb')
    pickle.dump(customer, output_file)
    output_file.close()

def view_account(customer):
    pass
    cust_profile = input('Enter a customer ID to look up: ')
    print(cust_profile.get(id, 'Customer not found'))

    # Customer-side menu

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