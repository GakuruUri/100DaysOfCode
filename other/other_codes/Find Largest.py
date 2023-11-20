count = 1
print('Enter x to exit the program: ')
print('Enter three numbers! ')
num1 = input('Enter The First Number: ')
if num1 =='x':
    exit()
else:
    num1 = int(num1)
    num2 = int(input('Enter The Second Number: '))
    num3 = int(input('Enter The Third Number: '))
    largest = num1
    if largest < num2:
        if num2 > num3:
            largest = num2
        else:
            largest = num3
    elif largest < num3:
        if num3 > num2:
            largest = num3
        else:
            largest = num2
    else:
        largest = num1
    if (num1 == num2 and num2 == num3):
        count = 0
    if count == 0:
        print('All The Numbers Are Equal')
    else:
        print('Largest Of The Numbers Is: ' + str(largest)) 

