
# 🎮 Hangman Game Challenge

## 🎯 Objective

Build a Hangman game in Python that uses loops, conditionals, and user input to let a player guess a hidden word before attempts run out.

## 📝 Tasks

### 🛠️ Build the Hangman game loop

#### Description
Create a game loop that selects a random word, prompts the player for letter guesses, updates the display, and ends when the player wins or loses.

#### Requirements
Completed program should:

- Select a random word from a predefined list
- Prompt the player to guess one letter at a time
- Show the current word progress using blanks and revealed letters
- Track and display the number of incorrect guesses remaining
- End the game with a win or lose message

### 🛠️ Handle user input and game state

#### Description
Validate user guesses and keep track of letters guessed so far so players cannot repeat the same guess.

#### Requirements
Completed program should:

- Ignore repeated letter guesses and prompt the player again
- Prevent invalid input from breaking the game
- Show the letters that have already been guessed
- Update the display after each valid guess
