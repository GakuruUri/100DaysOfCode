"""
10-6. Addition: 
One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a ValueError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. Test your 
program by entering two numbers and then by entering some text instead of a 
number.

"""

"""
# A program that adds 2 numbers - simple calculator.
print("Give me two numbers and i will add them for you.\n")

try:
    x = int(input("Enter your first number: "))
    y = int(input("Enter your second number: "))


    print(x + y)
except ValueError:
    print("Please enter an integer.")
"""  
    
# Second Option

try:
    x = input("Give me a number: ")
    x = int(x)
    
    y = input("Give me a second number: ")
    y = int(y)
    
except ValueError:
    print("Sorry, I really need a number. ")

else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")