import pickle
import BankAccount

FILE = customers.txt

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
                show_accounts()
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
        input_file = open(FILE, 'r')
        cust_list = input_file.load(input_file)
        input_file.close()
    except IOError:
        cust_list={}
    return cust_list

def change(customer):
    name = input("Who's information would you like to change: ")
    if name in customer:
        name = input('Enter the new name: ')
        balance = float(input('Enter the new balance: '))
        interest = input('Enter the new interest rate: ')
        entry = account.BankAccount(name, balance, interest)
        customer[name] = entry
        print('Information updated.')
    else:
        print('That name is not found.')

def save_customers(customer):
    output_file=open(FILE, 'w')
    file.write(customer, output_file)
    output_file.close()

def view_account():
    pass
    # parse list and view info specific to customer