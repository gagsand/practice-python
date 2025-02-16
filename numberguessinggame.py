import random

answer = random.randint(1, 100)

while True:
    player_guess = int(input("Guess a number between 1 - 100: "))

    if player_guess < answer:
        print("Too low!")

    elif player_guess > answer:
        print("Too high!")

    elif player_guess == answer:
        print("Correct, you win!")
        break

    else:
        print("Invalid response")
