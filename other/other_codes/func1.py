import random
def getNumber(number):
    if number == 1:
        return 'The number is 1'
    elif number == 2:
        return 'The number is 2'
    elif number == 3:
        return 'The number is 3'
    elif number == 4:
        return 'The number is 4'
    elif number == 5:
        return 'The number is 5'
random_number = random.randint(1,5)
pick = getNumber(random_number)
print(pick)
    
