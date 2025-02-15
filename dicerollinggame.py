# programming with Mosh Youtube tutorial called "python projects for beginnners - master problem solving!"

# Loop
# ask user a question: roll the dice?
# if user enters y
#   generate two random numbers
#   print them
# If user enters n
#   print thank you message
#   Terminate
# Else
#   print invalid choice


import random

while True:
    player_input = input("Would you like to roll the dice? (y/n): ").lower()

    if player_input == "y":
        roll_dice1 = random.randint(1, 6)
        roll_dice2 = random.randint(1, 6)
        print(f'({roll_dice1}, {roll_dice2})')

    elif player_input == "n":
        print("thanks for playing")
        break

    else:
        print("Invalid choice, please enter y or n")
