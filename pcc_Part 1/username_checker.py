        
# Checking username 5-10  
current_users = ['Admin', 'gakuru', 'munjiru', 'waithera', 'mutuku']

new_users = ['admin', 'karanja', 'wanjiku', 'mukuru', 'mutuku']

for new_user in new_users:
    if new_user.lower() in (user.lower() for user in current_users):
        print(f"Sorry {new_user}, That name is already taken.")
        
    else:
        print(f"Heeeeey, {new_user}, the name is available.")



# List of current users (mixed case)
current_users = ['Alice', 'bob', 'CHARLIE', 'David', 'Eve']

# List of new users (mixed case)
new_users = ['Frank', 'GEORGE', 'alice', 'HARRY', 'Bob', 'alice']

# Loop through the new_users list
for new_user in new_users:
    # If the lowercase version of the new username is in the lowercase versions of current_users
    # Use of generator expressions.
    if new_user.lower() in (user.lower() for user in current_users):
        print(f"Username {new_user} is already in use. Please enter a new username.")
    else:
        print(f"Username {new_user} is available.")
        
        