import random
import time


wrong=0
questions=5
Min_operator=1
Max_operator=10
operators=['+','-','*']

def generator_problems():
    exp=str(random.randint(Min_operator,Max_operator))+random.choice(operators)+str(random.randint(Min_operator,Max_operator))
    answer=eval(exp)
    return exp,answer


print("Let's begin :)")
input("Press Enter if you are ready ")
start_time=time.time()

for i in range(questions):
    exp,ans=generator_problems()
    while True:
        guess=input(f"Problem{i+1}. {exp}=")
        if guess==str(ans):
            print("Correct! ")
            break
        wrong+=1
end_time=time.time()

total_time=end_time-start_time

print("You took ",round(total_time)," seconds to answer all questions ")
print("You gave",wrong," wrong answers")