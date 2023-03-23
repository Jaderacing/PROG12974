import BankAccount
import random

INTEREST_MODIFIER = 1
INTEREST_CUTOFF = 5000


def main():
    list = create_cust()
#    lookup(list)
#    update_cust(list)
    for key in list:
        print(key, list[key])

def create_cust():
    customer_list = {}
    while(True):
        try:
            numberOfCustomers = int(input('\nHow many customers would you like to create?: '))
            
            if numberOfCustomers <= 100:
                for customer in range(numberOfCustomers):
                    print(f'Creating customer #{customer+1}:')
                    cust_name = input('Please enter the name of the customer: ')
                    cust_id = random.randint(100000, 999999)
                    balance = 6500 # random.randint(1000, 7500)
                    baseInterest = float(input('Please set the users interest rate: '))
                    highInterest = baseInterest + INTEREST_MODIFIER
                    cutoff = INTEREST_CUTOFF
                    account = BankAccount.BankAccount(cust_name, cust_id, baseInterest, highInterest, cutoff, balance)
                    customer_list[cust_name] = account
                print(f'{numberOfCustomers} new customers have been created.')
            else:
                print('Please create no more than 100 new customers!')
                continue  
        except ValueError:
            print('Invalid input; please try again!')
            continue
        return customer_list
def lookup(account):
    name = input('Please input the name: ')
    print(name, account[name])

def update_cust(account):
    name = input('Please enter a name to update: ')
    if name in account:
        base_interest = input("Would you like to update the interest rate (y/n): ")
        if base_interest == "n":
            print('Value not updated')
        else:
            try:
                new_base_interest = float(input('Please enter the new interest rate: '))
                high_interest = new_base_interest + INTEREST_MODIFIER
                print('Customer updated.')
            except ValueError:
                print("Invalid input. Value not updated")
        balance = input("Would you like to input a new balance (y/n): ")
        if balance == "n":
            print('Value not updated')
        else:
            try:
                new_balance = float(input('Please enter a new balacne: '))
#                BankAccount.setBalance(new_balance)
                print('Customer updated.')
            except ValueError:
                print("Invalid input. Not updated")
        update = BankAccount.BankAccount(name, id, new_base_interest, high_interest, cutoff, new_balance)
        account[name] = update
    else:
        print('Customer not found')

main()