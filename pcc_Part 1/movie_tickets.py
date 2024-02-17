age = int(input("What is your age: "))

if age < 3:
    print("Your ticket is free.")
elif age > 3 and age < 12:
    print("Your ticket is $10")
else:
   print("Your ticket is $15")
   

while True:
    age = input("Enter your age (or 'quit' to finish): ")
    if age.lower() == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")


'''Using a conditional test in the while statement to stop the loop:'''

age = ''
while age.lower() != 'quit':
    age = input("Enter your age (or 'quit' to finish): ")
    if age.lower() != 'quit':
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
            
            
##################
'''Using an active variable to control how long the loop runs:'''
active = True
while active:
    age = input("Enter your age (or 'quit' to finish): ")
    if age.lower() == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
            
'''Using a break statement to exit the loop when the user enters a ‘quit’ value:'''           
            
while True:
    age = input("Enter your age (or 'quit' to finish): ")
    if age.lower() == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")

