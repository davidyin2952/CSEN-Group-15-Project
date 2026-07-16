import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "keyboard"]
    return random.choice(words)

def play_game():
    word = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")

    while attempts_left > 0:
        current_display = ""
        for letter in word:
            if letter in guessed_letters:
                current_display += letter
            else:
                current_display += "_"

        print("\nWord: " + current_display)
        print("Attempts left:", attempts_left)

        if current_display == word:
            print("You win! The word was:", word)
            return

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts_left -= 1
            print("Wrong guess!")

    print("\nGame over! The word was:", word)

if __name__ == "__main__":
    play_game()
