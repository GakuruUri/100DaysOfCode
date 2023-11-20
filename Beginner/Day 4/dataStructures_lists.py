# Randomize a list

import random

all_names = input("Give me everybody's names, separated by a comma: ")

names = all_names.split(", ")


# #Get total number of peaple
# num_items = len(names)


# #First Method
# random_choice = random.randint(0, num_items - 1)
# payer = names[random_choice]

# print(f"{payer} is going to pay for your meal today.")

#Second Method
to_pay = random.choice(names)
print(f"{to_pay} is going to pay for your meal tomorrow.")