bob_marley = {
    'first_name': 'Bob',
    'last_name': 'Marley',
    'age': 35,
    'city': 'nine miles',
}

for key, value in bob_marley.items():
    print(f"\n{key}: {value}")


# Define a dictionary to store information about a person
person = {
    "first_name": "Uri",
    "last_name": "Gakuru",
    "age": 37,
    "city": "Nairobi"
}

# Print each piece of information stored in the dictionary
for key, value in person.items():
    print(f"\n{key}: {value}")



# Try it yourself 6-7 People

bob_marley = {
    'first_name': 'Bob',
    'last_name': 'Marley',
    'age': 35,
    'city': 'nine miles',
}

alice_smith = {
    'first_name': 'Alice',
    'last_name': 'Smith',
    'age': 30,
    'city': 'New York',
}

charlie_johnson = {
    'first_name': 'Charlie',
    'last_name': 'Johnson',
    'age': 40,
    'city': 'London',
}

people = [bob_marley, alice_smith, charlie_johnson]

for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print("\n")
