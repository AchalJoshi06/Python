
def deposite():
    while true:
        amount=input("Enter the amount you wanna add(USD) : \n")
        
        if amount.isdigit():
            amount=int(amount)
            
            if amount > 0:
                break
            else:
                print("Amount must be greater then zero.")
        
        else:
            print("please enter a valid amount .")
            
        return amount
              