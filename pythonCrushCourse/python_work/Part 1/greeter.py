name = input("Please enter your name: ")

print(f"\nHello, {name}!")


prompt = "If you share your name, we can personalize the message you see."
prompt += "\nwhat is your first name? "


name = input(prompt)
print(f"\nHello, {name}!")

# Defining a finction.

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()


# Passing information to a function
print("\n===Pass info to a function.===")
def greet_user(username):
    # Display a simmple greeting
    print(f"Hello, {username.title()}!")

greet_user('Gakuru')


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# Adding a break statement to exit the loop.

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


def get_formatted_name(first_name, last_name):
    """Returns the formatted name."""
    full_name = f"{first_name}{last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("first name: ")
    if f_name == "q":
        break
    
    l_name = input("last name: ")
    if l_name == "q":
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")