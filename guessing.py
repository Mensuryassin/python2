import random

def guessing_game():
    secret_number = random.number(1, 100)

    print("Welcome to the guessing Game!")
    print("I'm thinking of a number betweem 1 and 100.")

    attempts = 0

    while True:
        guess = input("take a guess: ")

        if not guess.isdigit():
            print("Please enter a Valid number.")
        continue
        
        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"congratulations! you guessed the number in {attempts} attempts!")
            break
guessing_game