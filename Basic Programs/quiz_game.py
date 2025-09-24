Name =input("Enter your name : ")
print("Hello",Name)

play=input("You want to play One Piece Anime Quiz ?")

if play!="yes":
    quit()
 
print(Name,"Let's Play One Piece Anime Quiz😆😆")
score = 0

print("let's move to frist Question.\n\n")


Q1=input("WHAT IS THE REAL NAME OF WHITE BEARD?\n")
if( Q1=="Edward Newgate"):
    print("Yeee !your ans is correct")
    score +=1
else:
    print("Sorry! You got wrong Ans.")
    
    print("let's move to frist Question.\n\n")

Q2=input("Which devil Fruit Luffy eat?\n")
if( Q2=="Human Human Fruit:NIKA modal "):
    print("Yeee !your ans is correct")
    score +=1
else:
    print("Sorry! You got wrong Ans.")
    
    print("let's move to next Question.\n\n")

Q3=input("Which Devil Fruit is best?\n")
if( Q3=="Dark Dark Fruit " or "Human Human Fruit:NIKA modal"):
    print("Yeee !your ans is correct")
    score +=1
else:
    print("Sorry! You got wrong Ans.")

print("let's move to next Question.\n\n")

Q4=input("Is luffy's fate already decided by GOL D. ROGER?\n")
if( Q4=="yes"):
    print("Yeee !your ans is correct")
    score +=1
else:
    print("Sorry! You got wrong Ans.")
    
    print("let's move to next Question.\n\n")


Q5=input("Who is the strogest swordsman in one piece?\n")
if( Q5=="Dracule Mihawk" or "Hawk-Eye"):
    print("Yeee !your ans is correct")
    score +=1
else:
    print("Sorry! You got wrong Ans.")
    
    
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")

print("THANK YOU FOR PLAYING OUR QUIZ.\n\n")