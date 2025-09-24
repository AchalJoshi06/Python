import random
import time

OPERATORS =["+","-","*"]
MIN_OPERANDS=3
MAX_OPERANDS=12

TOTAL_PROBLEMS=10

def generate_problem():
    left=random.randint(MIN_OPERANDS,MAX_OPERANDS)
    right=random.randint(MIN_OPERANDS,MAX_OPERANDS)
    operator = random.choice(OPERATORS)
    
    expr = str(left) + " " + operator + " " +str(right) 
    answer = eval(expr)
    return expr,answer

wrong=0

input("press any key to start.")
print("-------------------------")

start_time=time.time()

for i in range(TOTAL_PROBLEMS):
    expr,answer = generate_problem()
    while True:
        guess =input("problem #" + str(i+1) + ":  "+expr + "=")
        
        if guess == str(answer):
            break
        wrong+=1
        
end_time=time.time()
total_time=end_time-start_time
        
print("-------------------------")
print("Nice Work! ypu completed in ",total_time,"seconds.")