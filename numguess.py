import random
import math 

print("Hi welcome to the game, This is a number guessing game.\n Let's start the game")
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

x = random.randint(lower, upper) 

total_chances = math.ceil(math.log(upper - lower + 1,2))

print("\n\tYou've only ", total_chances, " chances to guess the integer!\n")
count = 0
flag = False 


while count < total_chances :
    count += 1

    guess = int(input("Your guess number is: "))

    if x == guess :
        print("Congratulations you did it in ",count, " try!")

        flag = True 
        break 

    elif x > guess :
        print("You guessed too small")
    elif x < guess :
        print("You guessed too high")