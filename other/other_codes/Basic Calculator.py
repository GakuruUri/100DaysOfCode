# Basic Calculator

def Addition(number1, number2):
    result = number1 + number2
    print('The Result is: ' + str(result))

def Subtract(number1, number2):
    result = number1 - number2
    print('The Result is: ' + str(result))

def Multiplication(number1, number2):
    result = number1 * number2
    print('The Result is: ' + str(result))

def divide(number1, number2):
    result = number1 / number2
    print('The Result is: ' + str(result))

print ('1. Addition')
print ('2. Subtraction')
print ('3. Multiplication')
print ('4. Division')
print ('5. Exit')

while True:
    choice = int(input('Enter Your Choice: '))
    if (choice >=1 and choice <=4):
        print ('Enter 2 Numbers')
        num1 = int(input('Enter a First number: '))
        num2 = int(input('Enter a Second Number: '))
        if choice == 1:
            Addition(num1,num2)
        elif choice == 2:
            Subtract(num1,num2)
        elif choice == 3:
            Multiplication(num1,num2)
        else:
            divide(num1,num2)
    elif choice == 5:
        break
    else:
        print('You Entered a  wrong Choice!!!')