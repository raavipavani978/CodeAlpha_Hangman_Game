# 🎮 Hangman Game

A simple **text-based Hangman Game** developed using Python as part of the **CodeAlpha Python Programming Internship**.

## 📌 Description

The Hangman Game randomly selects a word from a predefined list. The player attempts to guess the word by entering one letter at a time.

The player is allowed a maximum of **6 incorrect guesses**. The game ends when the player successfully guesses the complete word or uses all available chances.

## ✨ Features

* 🎲 Randomly selects a word from a predefined list
* 🔤 Allows the user to guess one letter at a time
* ❌ Maximum of 6 incorrect guesses
* 🔁 Prevents repeated letter guesses
* ✅ Validates user input
* 🏆 Displays a winning message when the word is guessed
* 💀 Displays a game-over message when all chances are used

## 🛠️ Technologies Used

* **Python 3**
* `random` module
* Lists
* Strings
* Loops
* Conditional statements
* User input

## 📂 Project Structure

```text
CodeAlpha_HangmanGame/
│
├── hangman.py
├── README.md
```

## ▶️ How to Run

### 1. Make sure Python 3 is installed

Check your Python version:

```bash
python --version
```

### 2. Run the game

Open the terminal in the project folder and execute:

```bash
python hangman.py
```

## 🎮 How to Play

1. The computer randomly selects a word.
2. The selected word is displayed using underscores.
3. Enter one letter at a time.
4. Correct letters are revealed.
5. An incorrect letter reduces the remaining chances.
6. You have a maximum of **6 incorrect guesses**.
7. Guess the complete word to win the game.

## 💻 Example

```text
===================================
      WELCOME TO HANGMAN GAME
===================================
Guess the word one letter at a time!
You have 6 incorrect guesses.

Word: _ _ _ _ _ _

Enter a letter: p
✅ Correct!

Word: p _ _ _ _ _
```

## 🧠 Concepts Demonstrated

This project demonstrates basic Python programming concepts including:

* Random word selection
* Lists and strings
* `while` loops
* `for` loops
* `if-else` conditions
* User input validation
* Tracking guessed letters

## 🚀 Future Improvements

Possible improvements for future versions include:

* Adding difficulty levels
* Adding a scoring system
* Adding more words
* Adding hints
* Creating a graphical user interface
* Adding a visual Hangman figure

## 👨‍💻 Author

**Raavi Pavani**

Python Programming Intern
**CodeAlpha Internship**

## 📌 Internship Task

This project was developed as part of the **CodeAlpha Python Programming Internship – Python Programming Task: Hangman Game**.
