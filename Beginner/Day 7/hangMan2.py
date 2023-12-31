# Step 2

import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Psssst, the solution is {chosen_word}.')

'''
 TODO-1 - Create an empty list called display. For each letter in the chosen_word, add a "_" to "display". So if the
 chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
'''
display = []  # Create an empty list
word_length = len(chosen_word)  # Since len(chosen_word) is used severally, we create a variable to hold that
# for letter in chosen_word:
for _ in range(word_length):
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

# TODO-2 - Loop through each position in the chosen word;

'''
# if the letter at teh position matches 'guess' then reveal that letter in the display at the position.
# eg if the user guesses "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"]

# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")
'''
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

# TODO-3 -print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
print(display)
