"""
10-7. Addition Calculator:
Wrap your code from Exercise 10-5 in a while loop
so the user can continue entering numbers, 
even if they make a mistake and
enter text instead of a number
"""
# print("Enter 'q' at anytime to quit.\n")

# while True:


#     #print("Give me two numbers and i will add them for you.\n")

#     try:
#         x = int(input("Enter your first number: "))
#         if x == 'q':
#             break
#         y = int(input("Enter your second number: "))
#         if y == 'q':
#             break


#     except ValueError:
#         print("Please enter an integer.\n")
        
#     else:
#         sum = x + y
#         print(sum)



print("Enter 'q' at any given time to quit.\n")

while True:
    try:
        x = input("\nGivve me a number: ")
        if x == 'q':
            break
        x = int(x)
        
        y = input("Give me another number: ")
        if y == 'q':
            break
        y = int(y)
        
    except ValueError:
        print("Sorry, I really need a number.")
        
    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")

        
            