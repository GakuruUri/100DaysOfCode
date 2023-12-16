"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop through
the list of sandwich orders and print a message for each order, such as I made
your tuna sandwich. As each sandwich is made, move it to the list of finished
sandwiches. After all the sandwiches have been made, print a message listing
each sandwich that was made.
"""	


print("\n =====My loop=====")

sandwich_orders = ['swahili','pastrami', 'taco']
finished_sandwiches = []


# Verifying there are no more sandwiches ordered
# Move each verified sandwich to finished_sandwiches

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()


    print(f"I made your {current_sandwich} sandwich😁.")
    finished_sandwiches.append(current_sandwich)



# Display all sandwiches.

print("\nThe following sandwiches have been made🍔🍕.")
for confirmed_sandwich in finished_sandwiches:
    print(confirmed_sandwich.title())


"""
7.8 Deli code chatGPT
"""

print("\n =====The chatGPT while loop=====")

# List of sandwich orders

sandwich_orders = ['tuna', 'chicken', 'beef', 'veggies', 'turkey']


# Empty list of finished sandwiches
finished_sandwiches = []


# Loop through the list of sandwich orders using a while loop
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)

    print(f"I made your {current_sandwich} sandwich.")

    # As each sandwich is made, move it to list of finished sandwiches.
    finished_sandwiches.append(current_sandwich)


# After all the sandwiches have been made, print a message listing each sandwich that was made.
print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)

"""
A for loop
When you run this code, it will make each sandwich in the sandwich_orders list, and then print a list of all sandwiches that were made. Enjoy your meal! 😊
"""
print("\n =====The for loop=====")

# List of sandwich orders
sandwich_orders = ['tuna', 'chicken', 'beef', 'veggie', 'turkey']


# Create an empty list of sandwiches
finished_sandwiches = []


# Loop through the list of sandwiches
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    # As each sandwich is made, move it to the list of finished_sandwiches
    finished_sandwiches.append(sandwich)


#After all the sandwiches have been made, print a message listing each sandwich that was made.
print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)





























































