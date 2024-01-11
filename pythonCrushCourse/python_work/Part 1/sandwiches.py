""" 
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that’s being ordered. Call the function three times, using a different number
of arguments each time.

"""

def sandwich_ingredients(*args):
    """Print a summary of sandwich ingredients being ordered."""
    print("\nThese are the sandwich ingredients:")
    for arg in args:
        print(f"-{arg}")


sandwich_ingredients()
sandwich_ingredients('salad', 'cucumber', 'chicken')
sandwich_ingredients('salad', 'cucumber', 'chicken', 'tuna')