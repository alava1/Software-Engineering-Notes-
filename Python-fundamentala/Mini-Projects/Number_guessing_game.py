# number_guessing_game.py
# Fun Project: Number Guessing Game

import random

print("=== Number Guessing Game ===\n")

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts.\n")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts+1}/{max_attempts} - Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try higher.")
        elif guess > secret_number:
            print("Too high! Try lower.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            break
    except ValueError:
        print("Please enter a valid number.")

if attempts == max_attempts and guess != secret_number:
    print(f"😔 Game Over! The number was {secret_number}.")
