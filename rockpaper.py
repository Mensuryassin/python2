import random

def determine_winner(player, computer):
    if player == computer:
        return "its a tie!"
    elif (player == "rock" and computer == "scissors") or \
        (player == "scissors" and computer == "paper") or \
        (player == "paper" and computer == "rock"):
        return "You Win!"
    else: 
        return "computer Win!"

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")

    choices = ['rock', 'papper', 'scissors']

    while True:
        player_choice = input("Enter rock, paper or scissors(or 'quit' to stop): ").lower()
        if player_choice == "quit":
            print("thanks for playing! Goodbye!")
            break
        elif player_choice not in choices:
            print("Invalid choice. please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer Chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print

rock_paper_scissors()