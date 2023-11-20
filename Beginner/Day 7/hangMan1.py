# Step 1

word_list = ["ardvark", "baboon", "camel"]  # The List
# TODO -1- Randomly choose a word from the word_list and assign it to a variable called chosen_word.

import random

chosen_word = random.choice(word_list)  # Randomize list

# TODO -2- Ask the user to guess a letter and assign the answer to a variable called guess. Make guess lower case

guess = input("Guess a letter: ").lower()  # User input, assign to list and and make it lower

# TODO -3- Check if the letter the user guessed(guess) is one of the letters of the chosen word(for loop)

for letter in chosen_word:  # For loop checker
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
