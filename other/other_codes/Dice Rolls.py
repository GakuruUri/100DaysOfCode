# Dice Game

import random

min = 1
max = 6

roll_dice = "yes"

while roll_dice == "yes" or roll_dice == "y":
    print ("The Values are....")
    print (random.randint (min,max))
    print (random.randint (min,max))

    roll_dice = input("Roll the Dice again? ")
else:
    print ("Thank you for Playing! ")