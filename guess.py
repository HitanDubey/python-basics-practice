import numpy as np
import random

num = random.randint(1,10)
print("Welcome to the game")
guess = -1
while guess != num:
    guess =int(input("Enter your guess : "))

    if guess < num:
        print("You guess is low")
    elif guess > num :
        print("You guess is  high")
    else:
        print("you guess correct!")