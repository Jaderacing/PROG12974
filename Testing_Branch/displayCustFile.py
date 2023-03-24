import BankAccount
import random
import pickle

INTEREST_MODIFIER = 1
INTEREST_CUTOFF = 5000


def main():
    list = create_cust()
    display_customers()

def create_cust():
    customer_list = {}
    while(True):
        try:
            numberOfCustomers = int(input('\nHow many customers would you like to create?: '))
            if numberOfCustomers <= 100:
                for customer in range(numberOfCustomers):
                    print(f'Creating customer #{customer+1}:')
                    cust_name = 'Dave'
                    cust_id = random.randint(100000, 999999)
                    balance = random.randint(1000, 7500)
                    baseInterest = 2.5
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

def display_customers():
    end_of_file = False
    input_file = open('customers.dat', 'rb')
    cust_dict = {}
    while not end_of_file:
        try:
            cust = pickle.load(input_file)
            cust_dict[cust.self.__name()] = cust

            print(f'Name is {cust.self.__name()}\n')
            print(f'Name is {cust.self.__id()}\n')
            print(f'Name is {cust.self.__balance()}\n')
            print(f'Name is {cust.self.__interestRate()}\n')

        except EOFError:
            end_of_file = True
    input_file.close()

if __name__ == '__main__' :
    main()