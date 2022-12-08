pin = 255609
i = 0 
chances = 3
guess = 0

def landing():
    print("""

        WELCOME TO ATM MACHINE

---------------------------------------------

    """)

landing() 

def options():
    print("""
    
    press '1' to deposit
    press '2' to withdraw
    press '3' to check balance

    """)


def deposit():
    amount = float(input("AMOUNT TO DEPOSIT: "))
    limit = 1000000
    if amount < limit:
       global i 
       i += amount
       print(f"DEPOSITED AMOUNT: {i}")
    elif amount > limit:
        print(f"Deposit limit is {limit}")
    
    
def withdraw():
    limit = 3
    guesses = 0
    while guesses < limit:
        user = int(input("enter PIN: "))                        
        guesses += 1
        chances = limit - guesses
        if user == pin:
            amount = float(input("AMOUNT TO WITHDRAW: "))
            if amount  < i:
                global total
                total = i - amount
                print(f'Withdrawn Amount: {amount}  New Balance: {total}') 
                break            
            elif amount > i:
                print("Insufficient balance") 
                break
        elif user != pin:
            print(f"INCORRECT PASSWORD, chances: {chances}") 
            

def check():
        print(f"BALANCE: {total}")            


while guess < chances:
    user_pin = int(input("Enter 6 number pin: "))
    guess += 1
    if user_pin == pin:
        while True:
            user = int(input("\nDo you want to continue? (1) yes (0) no: "))
            if user == 1:
                options()
                user_option = int(input("choose one: "))
                if user_option == 1:
                    deposit()
                    continue
                elif user_option == 2:
                    withdraw()
                    continue
                elif user_option == 3:
                   check()
                   continue
                elif user_option != 1 and 2 and 3:
                    print("Enter correct number to proceed")
                    continue
            elif user != 0 and 1:
                print("enter correct number to proceed!")    
                continue
            elif user == 0:
                print("Thank you for your time")   
            break
        break
    else:
        print("Incorrect Password! \n")     
      
print("SYSTEM TERMINATED\n")
        

