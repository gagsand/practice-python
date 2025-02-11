# programming with Mosh Youtube tutorial called "python projects for beginnners - master problem solving!"

import random

player_input = input("Roll the dice? (y/n): ").lower()


if player_input == "y":
    while True:
        roll_dice1 = random.randint(1, 6)
        roll_dice2 = random.randint(1, 6)
        print((roll_dice1, roll_dice2))
        break

if player_input == "n":
    print("thanks for playing")
