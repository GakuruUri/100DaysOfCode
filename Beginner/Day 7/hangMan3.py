# Step 3

import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code

print(f"Pssst, the solution is {chosen_word}.")


#create blanks
display = []

for _ in range  (word_length):
    display += "_"

#TODO - 1 - use the while loop to let the user guess again . 
# the loop should only stop once the user has guessed all the letters in the chosen word and 'display' has no more blanks ("_").
# Then you can tell the user they've won


end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position:{position} \n Current letter:{letter}\n Guessed letter:{guess} ")
        if letter == guess:
            display[position] = letter

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You Win")