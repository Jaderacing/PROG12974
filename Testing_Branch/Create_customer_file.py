# Menu for selecting which user branch to use
# Date v1.0 2023-03-16

import BankAccount
import random
import pickle

account = BankAccount.BankAccount

def main():
    create_cust_file()

def create_cust_file():
    while(True):
        try:
            customer_file = open('bankfile.dat', 'wb')
            numberOfCustomers = int(input('\nHow many customers would you like to create?: '))

            if numberOfCustomers >= 10 and numberOfCustomers <= 100:
                for customer in range(numberOfCustomers):
                    print(f'Creating customer #{customer+1}:')
                    cust_name = input('Please enter the name of the customer: ')
                    cust_id = random.randint(100000, 999999)
                    balance = random.randint(1000, 5000)
                    interest_rate = float(input('Please set the users interest rate: '))
                    account = BankAccount.BankAccount(cust_name, cust_id, interest_rate, balance)
                    pickle.dump(account, customer_file)
                customer_file.close()
                print(f'File has been created with: {numberOfCustomers} new customers.')
                break
            else:
                print('Please create no less than 10, and no more than 100 customers!')
                continue  
        except ValueError:
            print('Invalid input; please try again!')
            continue
        finally: # Just incase something happens 
            customer_file.close()

if __name__ == '__main__':
    main()