# Guess Numbers

import random

# Defining Variables

n = random.randint (1, 99)
guess = int(input("Enter an integer From 1 to 99: "))

# Introduce a loop

while n != "guess":
    print
    if guess < n:
        print("Number Guessed is Low")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print("Guess is too high")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print("You Guessed It: ")
        break
    print