# rock, paper, scissors

import random

# we create a while loop that allows us to continue playing until were done
gameon = True

while gameon:
    # we create a list of the options to pick from.

    play = ['rock','paper', 'scissors']

    print("welcome To Rock Paper Scissors")

    # we make provision to allow the player and the computer to choose their option

    your_choice = input("you choose ..: ")
    computer_choice = random.choice(play)

    print(f"you chose {your_choice} and computer chose {computer_choice}")

    # we make an if statement to ensure the conditions are met before declaring the winner

    if your_choice == computer_choice:
        print("Its a tie, we have no winner")
    elif your_choice == 'rock' and computer_choice == 'scissors':
        print("You win")
    elif your_choice == 'scissors' and computer_choice == 'paper':
        print("you win")
    elif your_choice == 'paper' and computer_choice == 'rock':
        print("You win")
    else:
        print("you lose")

    #make a while loop to keep asking for a valid input
    while True:
        retry = input("would you like to continue :")
        if retry == 'yes':
            break
        elif retry == 'no':
            break
        else:
            continue

    # once the game is finished, ask if the user is done or would like to continue

    if retry== 'yes':
        gameon
    elif retry== 'no':
        print("good bye")
        gameon = False

