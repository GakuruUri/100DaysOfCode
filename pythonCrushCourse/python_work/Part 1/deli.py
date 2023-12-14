"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop through
the list of sandwich orders and print a message for each order, such as I made
your tuna sandwich. As each sandwich is made, move it to the list of finished
sandwiches. After all the sandwiches have been made, print a message listing
each sandwich that was made.
"""


sandwich_orders = ['swahili', 'pastrami', 'taco']
finished_sandwiches = []

# Verifying there are no more sandwiched ordered
# Move each verified sandwich to the finished list.
while sandwich_orders:
    current_sandwich  = sandwich_orders.pop()
    
    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)
    
    
    # Display all finished sandwiches.
    
print("\nThe following sandwiches have been made.")
for confirmed_sandwich in finished_sandwiches:
    print(confirmed_sandwich.title())
    
    

"""This code will do the same thing as the previous one, but it uses a while loop instead of a for loop. It will continue making sandwiches until there are no more sandwiches left in the sandwich_orders list. Enjoy your meal!"""


# List of sandwich orders
sandwich_orders = ['tuna', 'chicken', 'beef', 'veggie', 'turkey']

# Empty list of finished sandwiches
finished_sandwiches = []

# Loop through the list of sandwich orders using a while loop
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    # As each sandwich is made, move it to the list of finished sandwiches
    finished_sandwiches.append(current_sandwich)

# After all the sandwiches have been made, print a message listing each sandwich that was made
print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)
    
    
    
    
"""
When you run this code, it will make each sandwich in the sandwich_orders list, and then print a list of all sandwiches that were made. Enjoy your meal! 😊
"""    
# List of sandwich orders
sandwich_orders = ['tuna', 'chicken', 'beef', 'veggie', 'turkey']

# Empty list of finished sandwiches
finished_sandwiches = []

# Loop through the list of sandwich orders
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    # As each sandwich is made, move it to the list of finished sandwiches
    finished_sandwiches.append(sandwich)

# After all the sandwiches have been made, print a message listing each sandwich that was made
print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)
    
    
    
"""
Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.

This code will first remove all ‘pastrami’ sandwiches from the sandwich_orders list, and then it will make each of the remaining sandwiches. It will print a list of all sandwiches that were made, and you will see that no pastrami sandwiches end up in finished_sandwiches. Enjoy your meal!

""" 
    
# List of sandwich orders
sandwich_orders = ['tuna', 'chicken', 'beef', 'veggie', 'turkey', 'pastrami', 'pastrami', 'pastrami']

# Print a message saying the deli has run out of pastrami
print("The deli has run out of pastrami.")

# Use a while loop to remove all occurrences of 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Empty list of finished sandwiches
finished_sandwiches = []

# Loop through the list of sandwich orders using a while loop
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    # As each sandwich is made, move it to the list of finished sandwiches
    finished_sandwiches.append(current_sandwich)

# After all the sandwiches have been made, print a message listing each sandwich that was made
print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)
    
    

"""
Dream Vacation: Write a program that polls users about their dream vacation.
Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll.

This code will keep polling users about their dream vacation until there’s no one else to respond. After the polling is complete, it will print the results. Please note that this code needs to be run in an environment where input() function can be used, such as a Python shell or a Jupyter notebook. Enjoy your polling!
"""


# Empty dictionary to store the poll results
dream_vacation_poll = {}

# Polling flag
polling_active = True

while polling_active:
    # Prompt for the user's name and dream vacation
    name = input("\nWhat's your name? ")
    dream_vacation = input("If you could visit one place in the world, where would you go? ")

    # Store the response in the dictionary
    dream_vacation_poll[name] = dream_vacation

    # Check if anyone else is going to take the poll
    repeat = input("Would you like another person to respond? (yes/ no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, dream_vacation in dream_vacation_poll.items():
    print(f"{name.title()} would like to visit {dream_vacation.title()}.")