import random

def guess_number():
    global guess
    for i in range(1,4):
        print('Guess The Number!')
        guess = int(input('Enter a number btwn 1 and 20: '))

        if guess < secretNumber:
            print('Number Too Low')

        elif guess > secretNumber:
            print('Number Too High')
        else:
            break
    return guess
def check(guess,secretNumber):
    if guess == secretNumber:
        print('Congrats on Number')
    else:
        print('Better Luck Tena number ni ' + str(secretNumber))

secretNumber = random.randint(1,20)
print('I am Thinking of a Number')

guess = guess_number()
check(guess,secretNumber)