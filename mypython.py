'''
balance = 0

while True:
    
    print("\nPress 1 for deposit")
    print("Press 2 for withdraw")
    print("Press 3 for check balance")
    print("Press 4 to Exit\n")
    
    user_input = int(input("Please Enter Any: "))
    
    
    if user_input == 1:
        deposit = float(input("Enter amount to deposit:"))
        
        if deposit > 0:
            balance += deposit
            print (f"You have depositted Php {deposit}")
            print(f"Your new balance is Php {balance}")
        
        else:
            print("The amount to deposit must be more than Php 0.00")
    
    elif user_input == 2:
        withdraw = float(input("Enter amount to Withraw: "))
        
        if withdraw <= balance:
            balance -= withdraw
            print (f"You have successfully withdrawed Php {withdraw}") 
            print(f"The remaining balance is Php {balance}")
        
        elif balance == 0:
            print ("Balance Must be not zero")

        else:
            print(f"Invalid Amount. Amount must be less than or equal to {balance}")
    
    elif user_input == 3:
        print(f"Your balance is {balance}")
    
    elif user_input ==4:
        print ("Thank you!")
        break
    
    else:
        print("Invalid Input")
'''


def check_balance(balance):
    print (f"Your balance is Php. {balance}")

def deposit(balance):
    amount_to_deposit = float(input ("Enter amount to deposit: "))
    balance += amount_to_deposit 
    return balance


def withdraw(balance):
    amount_to_withdraw = float(input ("Enter Amount to withdraw: "))
    if amount_to_withdraw > balance:
        print ("Insufficinet amount.")
    else:
        balance -= amount_to_withdraw
        print (f"You have succesfully withdrawed Php {balance}")
        print(f"The new balance is Php {balance}")
    return balance


balance = 0
while True:
    print("\nPress 1 for Check Balance")
    print("Press 2 for Deposit")
    print("Press 3 for Withdraw")
    print("Press 4 to Exit\n")

    user_input = int(input("Please Enter Any: "))

    if user_input == 1:
        check_balance(balance)

    elif user_input == 2:
        balance = deposit(balance)

    elif user_input == 3:
        balance = withdraw(balance)

    elif user_input == 4:
        break

    else:
        print ("Invalid Input")

print("Thank you for using this.")