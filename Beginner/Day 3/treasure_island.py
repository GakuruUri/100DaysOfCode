print("Welcome to treasure island!")

print("Your Mission is to find the treasure")

choice1=input('You are at a cross road, where do you want to go: Type "Left" or "Right" ').lower()

if choice1 == "left":
    #continue with game
    choice2 = input('You\ve come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for boat or "Swim" to swim accross ').lower()
    if choice2 == "wait":
        #Game will continue
        choice3 = input("You arrive at a house with 3 doors, yellow, red and blue. Which one do you choose? ").lower()

        if choice3 == "red":
            print("You fell into a pit of fire, you lose")
        elif choice3 == "yellow":
            print("You found the treasure you win")
        elif choice3 == "blue":
            print("You enter a room full of beasts, you lose")
        else:
            print("That door doesnot exist game over")

    else:
        print("You got attacked by an angry trout. Game over")


else:
    print("You fell into a hole game over.")


    
