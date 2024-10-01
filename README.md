# Number Guessing Game

This is a simple Python number guessing game where the user tries to guess a randomly generated number within a specified range. The game will provide hints to guide the user and count the number of guesses made.

## How to Play

1. The game will ask you to choose an upper limit for the range of numbers.
2. The game will generate a random number between 0 and the upper limit you provided.
3. You will then try to guess the randomly generated number.
4. The game will guide you by telling you if your guess is above or below the target number.
5. The game continues until you guess the correct number.

## Features

- Input validation to ensure correct entries.
- Random number generation based on a user-specified range.
- Unlimited guesses with feedback on each guess (whether it is higher or lower than the target number).
- Tracks and displays the number of guesses taken to find the correct number.

## Usage

To play the game, run the Python script:

```bash
python guessing_game.py

Choose the upper limit: 20
Take a guess: 10
You are above the number.
Take a guess: 5
You are below the number.
Take a guess: 7
You got it!
The number of guesses: 3
```
