import random
import BankAccount

INTEREST_CUTOFF = 5000
INTEREST_MODIFIER = 1.5

def main():
    id = random.randint(100000, 999999)
    name = input('Please input customer name: ')
    baseInterest = float(input('Please input the BASE interest rate: '))
    highInterest = baseInterest + INTEREST_MODIFIER
    cutoff = INTEREST_CUTOFF
    balance = float(input('Please input the starting balance: '))
    account = BankAccount.BankAccount(name, id, baseInterest, highInterest, cutoff, balance)

    # deposit = float(input('Please input deposit: '))
    # while deposit < 0:
    #     float(input('Please input a positive number: '))
    # account.deposit(deposit)
    # print(f'${deposit:.2f} deposited. New balance is '
    # f'{account.getBalance():.2f}$')
    # print()
    print(str(account))
    print()
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
    print()
    print(str(account))

    # withdraw = float(input('Please input withdraw: '))
    # while withdraw >= account.getBalance():
    #     withdraw = float(input('Insufficient funds! Input new number: '))
    # account.withdraw(withdraw)
    # print(f'{withdraw:.2f}$ withdrawn. New balance is '
    # f'{account.getBalance():.2f}$')  
    # print()
    
    print(f'{account.getBalance():.2f}')
    print(f'{account.getInterestRate():.2f}')
    # print(f'{account.getMonthlyInterest():.2f}')
    # print()
    
    # print(str(account))

main()