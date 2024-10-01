import random

def get_random_word():
    words = ['python', 'java', 'hangman', 'computer', 'programming', 'artificial', 'intelligence','algorithm']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])


def hangman():
    print("welcome to hangman!")

    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_guesses = 6

    while incorrect_guesses < max_guesses:
        print(f"\nWorld: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses: {incorrect_guesses}/{max_guesses}")

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("you already guessed that letter")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good Guess! '{guess}' is in the world.")
        else:
            incorrect_guesses += 1
            print(f"sorry, '{guess}' os not in the word.")
        
        if all(letter is guessed_letters for letter in word):
            print(f"\nCongradulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()