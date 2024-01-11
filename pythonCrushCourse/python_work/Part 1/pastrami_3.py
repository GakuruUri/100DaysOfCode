"""
Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.

This code will first remove all ‘pastrami’ sandwiches from the sandwich_orders list, and then it will make each of the remaining sandwiches. It will print a list of all sandwiches that were made, and you will see that no pastrami sandwiches end up in finished_sandwiches. Enjoy your meal!

""" 
# List of sandwiches
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'chicken', 'pastrami', 'beef', 'veggie', 'turkey', 'pastrami']

# Print a message saying the deli has run out of pastrami.
print("The deli has run out of pastrami.")

# Use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
# Create an Empty list of finished sandwiches
finished_sandwiches = []

# Loop through the list of sandwich orders using a while loop
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    # As each sandwich is made, move it to the list of finished sandwiches.
    finished_sandwiches.append(current_sandwich)
    

# After all the sandwiches have been made, print a message listing each sandwich that was made.
print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)






