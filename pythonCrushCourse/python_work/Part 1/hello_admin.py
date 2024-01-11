# Hello Admin 5-8
users = ['admin', 'gakuru', 'munjiru', 'waithera', 'mutuku']

for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
        
# Option 2        
# List of users
users = ['Alice', 'Bob', 'Charlie', 'admin', 'Eve']

# Loop through the users list
for user in users:
    # If the username is 'admin'
    if user.lower() == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")

        
# No User test 5-9
users = []

if users:
    for user in users:
        print(f"Hello {user}, thank you for logging in again.")
        
else:
    print("We need to find some users!")       
        


# List of users
users = ['Alice', 'Bob', 'Charlie', 'admin', 'Eve']

# Check if the list of users is not empty
if users:
    # Loop through the users list
    for user in users:
        # If the username is 'admin'
        if user.lower() == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")

# Remove all of the usernames from the list
users = []

# Check again if the list of users is not empty
if users:
    # Loop through the users list
    for user in users:
        # If the username is 'admin'
        if user.lower() == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")




