import BankAccount
import random

INTEREST_MODIFIER = 1
INTEREST_CUTOFF = 5000


def main():
    list = create_cust()
    lookup(list)

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

main()