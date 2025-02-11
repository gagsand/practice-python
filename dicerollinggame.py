# programming with Mosh Youtube tutorial called "python projects for beginnners - master problem solving!"

import random

# answers = {"n": no, "y": yes}

player_input = input("Roll the dice? (y/n): ").lower()

if player_input != "y" or "no":
    print("invalid entry, try again")

if player_input == "y":
    while True:
        roll_dice = random.randint(1, 6)
        print(roll_dice)
        print(input("play again?: (y/n): "))

if player_input == "n":
    print("thanks for playing")
