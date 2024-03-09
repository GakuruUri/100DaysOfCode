# def greet_users(names):
#     """Print a simple greeting to each user in a list..."""
#     for name in names:
#         message = f"Hello, {name.title()}!"
#         print(message)
       
# username = ['hannah', 'ty', 'margot', 'uri']
# greet_users(username)


from pathlib import Path
import json

path =Path('username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")