# name = input("Please enter your name: ")

# print(f"\nHello, {name}!")


# prompt = "If you share your name, we can personalize the message you see."
# prompt += "\nwhat is your first name? "


# name = input(prompt)
# print(f"\nHello, {name}!")

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


