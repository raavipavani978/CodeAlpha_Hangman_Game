import random
# List of predefined words
words = ["python", "computer", "keyboard", "monitor", "internet"]
# Select a random word
word = random.choice(words)
# Variables to track the game
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6
# Welcome message
print("===================================")
print("      WELCOME TO HANGMAN GAME")
print("===================================")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")
print()
# Main game loop
while incorrect_guesses < max_incorrect:
    # Create the current display of the word
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word)
    # Check if the player has guessed the complete word
    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break
    # Ask the player for a letter
    guess = input("Enter a letter: ").lower()
    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue
    # Check for duplicate guesses
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    # Store the guessed letter
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("✅ Correct!")

    else:
        incorrect_guesses += 1
        print("❌ Wrong!")
        print(
            "Remaining Chances:",
            max_incorrect - incorrect_guesses
        )
# Game-over message
if incorrect_guesses == max_incorrect:
    print("\n💀 Game Over!")
    print("The word was:", word)
