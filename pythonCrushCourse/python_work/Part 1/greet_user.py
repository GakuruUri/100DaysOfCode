def greet_users(names):
    """Print a simple greeting to each user in a list..."""
    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)
       
username = ['hannah', 'ty', 'margot', 'uri']
greet_users(username)