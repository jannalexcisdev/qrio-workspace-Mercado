
balance = 0

while True:
    print("Press 1 for deposit")
    print("Press 2 for withraw")
    print("Press 3 for check balance")
    print("Press 4 to Exit")
    
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
        withraw = float(input("Enter amount to Withraw: "))
        
        if withraw <= balance:
            balance -= withraw
            print (f"You have successfully withrawed Php {withraw}") 
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


