"""
Dream Vacation: Write a program that polls users about their dream vacation.
Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll.

This code will keep polling users about their dream vacation until there’s no one else to respond. After the polling is complete, it will print the results. Please note that this code needs to be run in an environment where input() function can be used, such as a Python shell or a Jupyter notebook. Enjoy your polling!
"""

# Creat an empty dictionary to store the poll results.
dream_vacation_poll = {}

# Polling flag
polling_active = True

while polling_active:
    # Prompt the user's name and dream vacation.
    name = input("\nWhat is your name? ")
    dream_vacation = input("If you could visit one place in the world, where would you go? ")
    
    # Store the response in the dictionary.
    dream_vacation_poll[name] = dream_vacation
    
    # Check if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat.lower() == 'no':
        polling_active = False
        
        
# Polling is complete. Show results.
print("\n--- Poll Results ---")
for name, dream_vacation in dream_vacation_poll.items():
    print(f"{name.title()} would like to visit {dream_vacation.title()}")