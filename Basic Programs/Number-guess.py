import random
guess=0
top_of_range=input("Enter the Number :")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    
    if top_of_range<=0:
        print("Enter the number greater then 0.")
        quit()
else:
    print("Next time please enter the number.")
    quit()
        

random_number=random.randint(0,top_of_range)



while True:
    guess+=1
    user_guess=input("Enter your guess :")

    if user_guess.isdigit():
            user_guess=int(user_guess)
    else:
        print("Next time please enter the number.")
        continue

    if user_guess ==random_number:
        print("your guess is right.")
        break
    else:
        if user_guess>random_number:
            print("guess the lower number.")
        else:
            print("guess the grater number.")
        
print("you got it in ", guess ,"guesses")