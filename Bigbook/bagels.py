"""
Bagels, by Uri Gakuru urigakuru@live.co.uk
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle

"""


import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels, a deductive logic game.
16. By Al Sweigart al@inventwithpython.com
17.
18. I am thinking of a {}-digit number with no repeated digits.
19. Try to guess what it is. Here are some clues:
20. When I say: That means:
21. Pico One digit is correct but in the wrong position.
22. Fermi One digit is correct and in the right position.
23. Bagels No digit is correct.
24.
25. For example, if the secret number was 248 and your guess was 843, the
26. clues would be Fermi Pico.'''.format(NUM_DIGITS))
    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                # print('Guess is below 3 digits.')
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses. The answer was {}.'.format(secretNum))

        print('Do you want to play again? (yes or no)') 
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)
    
if __name__ == '__main__':
    main()
        






























