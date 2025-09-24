import random

computer_win=0
player_win=0

Choice=["rock","paper","scissors"]

while True:
    player_input=input("Enter your choice(Rock,Paper,Scissors,Q for quit):").lower()
    if player_input =="q":
        break
    
    if player_input not in Choice:
        continue
    
    random_number=random.randint(0,2)
    #rock=1 paper=2 scissor=3
    
    computer_choice=Choice[random_number]
    print("computer picked",computer_choice + ".")
    
    if (player_input=="rock" and computer_choice=="sicssors") or (player_input=="paper"and computer_choice=="rock" ) or (player_input=="scissors"and computer_choice=="paper") :
        print("you win!")
        player_win+=1
    else:
        print("you lose")
        computer_win+=1

print("you won ",player_win,"times.")
print("computer won ",computer_win,"times.")
print("GOODBYE.")



    