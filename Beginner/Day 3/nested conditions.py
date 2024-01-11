print("Welcome to the rollercoster")
height = int(input("What's Your Height in cms?"))
bill = 0
 
if height >= 120:
    print("You Can ride the rollercoster!")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("Child ticket 5 Dollars.")
    elif age <= 18:
        bill = 7
        print("Youth ticket 7 dollars.")
    else:
        bill = 12
        print("Adult 12 dollars")
        
        
    want_photo = input("Do you want a photo taken? Y or N. ")
    if  want_photo == "Y":
        bill +=3
    print(f"Your final bill is {bill}")
else:
    print("You are too short for the ride")