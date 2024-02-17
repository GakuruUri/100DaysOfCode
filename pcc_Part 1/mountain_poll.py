responses = {}
# Set a flag to indict that polling is active
polling_active = True


while polling_active:
    #Prompt for the person's name and respose.
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to climb?")
    
    
    # Store the response in a dictionary
    responses[name] = response
    
    
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        
        
# Polling is complete. Show results.

print("\n--- Polling Results ---")
for name, response in responses.items():
    print(f"{name} would you like to climb {response}.")



