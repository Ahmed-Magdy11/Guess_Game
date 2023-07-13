import math
import random
lower_num=int(input("Enter lower bound num "))
upper_num=int(input("Enter uppper bound num "))
chances=int(math.log2(upper_num-lower_num+1))
print(f"\n          You have only {chances} chances \n")
guss=int(input("Enter guss num "))
ran=random.randint(lower_num,upper_num)
count=0
while guss!=ran and chances:
    if guss>ran:
        print("Try Again! You guessed too high")
    elif guss<ran:
        print("Try Again! You guessed too small")
    count+=1
    chances-=1
    guss=int(input("Enter guss number "))

if not count:
    print("Wow , you are amazing you got it in first chance")
else:
    print(f"total gusses is = {count} to get the number" if chances else "Better Luck Next Time")