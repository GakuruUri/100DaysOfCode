# Looping through All Key-Value pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

# Looping through a dictionary using a for loop

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


# Second option for above

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for k, v in user_0.items():
    print(f"\n Key: {k}")
    print(f"Value: {v}")


