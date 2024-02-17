# Dictionaries of similar object

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}


# Lookup favorite language for a person who took the poll


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}


language = favorite_languages['sarah'].title()
print(f"\nSarah's favorite languages is {language}.")


# Looping through languages using a for loop
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")



# Looping through all Keys in a dictionary.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
 }

for name in favorite_languages.keys():
    print(name.title())
    
    
# Also below applies as we are looping through the keys which is the default
for name in favorite_languages:
    print(name.title())

print("\n")


# Accessing values associated with certain keys in a loop

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


# Using the keys() method to check if a value/key exists.


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")



 #Getting the dictionary in a particular order

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


# Looping through all values in a dictionary.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())




# Try it yourself 6.6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# List of people who should take the poll
people = ['jen', 'sarah', 'edward', 'phil', 'mike', 'lucy']

for person in people:
    if person in favorite_languages.keys():
        print(f"Thank you {person.title()} for taking the poll.")
    else:
        print(f"Hi {person.title()}, please take the poll.")
        
        

"""
In this script, favorite_languages is a dictionary 
that contains the names of people who have already 
taken the poll and their favorite languages. 
The people list contains the names of people who should 
take the poll. The script then loops through the people list. 
If a person’s name is found in the favorite_languages 
dictionary (meaning they have already taken the poll), 
a message is printed thanking them for taking the poll. 
If a person’s name is not found in the favorite_languages 
dictionary (meaning they have not yet taken the poll), 
a message is printed inviting them to take the poll. 
The title() function is used to ensure that the first 
letter of each person’s name is capitalized in the printed 
messages.

"""        
        
        
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}        

for name, languages in favorite_languages.items():
    if len(languages) == 2:
        print(f"{name}'s favorite languages are {languages}")
    else:
        print(f"{name}'s favorite language is {languages}")
        
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
        
        