"""
from pathlib import Path
import json

username = input("What is your name? ")

path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"We'll remeber you when you come back, {username}!")
"""


"""
We need to combine these two programs into one file
That is remember_me and greet_user.py
"""

# from pathlib import Path
# import json


# path = Path('username.json')
# if path.exists():
#     contents = path.read_text()
#     username= json.loads(contents)
#     print(f"Welcome back {username}!")

# else:
#     username = input("What is your name?")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     print(f"We'll remember you when you come back, {username}!")


"""
# Refactoring

from pathlib import Path
import json


def greet_user():
    # Greet the user by name.
    path = Path('username.json')

    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")

    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when come back, {username}")

greet_user()
"""


"""
Let’s refactor greet_user() so it’s not doing so many different tasks.
"""

# from pathlib import Path
# import json

# def get_stored_username(path):
#     #Get store username if available
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         return username

#     else:
#         return None

# def greet_user():
#     #Greet the user by name.
#     path = Path('username.json')
#     username = get_stored_username(path)

#     if username:
#         print(f"Welcome back, {username}!")

#     else:
#         username = input("What is your name? ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")

# greet_user()

"""
from pathlib import Path
import json


def get_stored_username(path):
    # Get stored username if available
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    # Prompt for a new username
    username = input("What is your name? ")
    contents = json.dumps(contents)
    path.write_text(contents)
    return username


def greet_user():
    # Greet the user by name.
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user

"""

"""
10-13. User Dictionary: The remember_me.py example only stores one piece of
information, the username. Expand this example by asking for two more pieces
of information about the user, then store all the information you collect in a 
dictionary. Write this dictionary to a file using json.dumps(), and read it back 
in using json.loads(). Print a summary showing exactly what your program
remembers about the user.
"""
from pathlib import Path
import json

def get_stored_user_info(path):
    """Get stored user info if available."""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
        
    else:
        return None
    
    
    
def get_new_user_info(path):
    """Get information from a new user."""
    username = input("What is your name? ")
    game = input("What is your favorite game? ")
    animal = input("What's your favorite animal? ")
    
    user_dict = {
        'username': username,
        'game': game,
        'animal': animal,
    }
    
    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict


def greet_user():
    """Greet the user by name, and state what we know about them. """
    path = Path('user_info.json')
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome back, {user_dict['username']}!")
        print(f"Hope you've been playing some {user_dict['game']}")
        print(f"Have you seen a {user_dict['animal']} recently?")
        
    
    else:
        user_dict = get_new_user_info(path)
        msg = f"We'll remember you when you return, {user_dict['username']}!"
        print(msg)
        
greet_user()
    




