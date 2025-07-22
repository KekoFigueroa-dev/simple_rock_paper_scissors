# Rock, Paper, Scissors Game

A Python implementation of the classic Rock, Paper, Scissors game where you compete against the computer over multiple rounds.

## How It Works

- Choose how many rounds you want to play
- Each round, pick rock, paper, or scissors
- The computer makes a random choice
- Winner is determined by classic rules:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock
- Scores are tracked and final winner is announced

## Implementation Features

- **Input validation**: Handles invalid inputs gracefully with try/except
- **Case-insensitive**: Accepts "ROCK", "rock", "Rock", etc.
- **F-string formatting**: Clean, readable output formatting
- **Score tracking**: Keeps track of wins/losses across all rounds
- **User-friendly errors**: Clear error messages for invalid inputs

## How to Run

```bash
python main.py

​
Sample Output
Welcome to a game of Rock, Paper, Scissors

How many rounds would you like to play?: 2

Round 1
Player: 0    Computer: 0
Time to pick...rock, paper, scissors: rock
    Computer: scissors
    Player: rock
    Rock smashes scissors!
    You win round 1.

Round 2
Player: 1    Computer: 0
Time to pick...rock, paper, scissors: paper
    Computer: rock
    Player: paper
    Paper covers rock!
    You win round 2.

Final Game Results
    Rounds Played: 2
    Player Score: 2
    Computer Score: 0
    Winner: PLAYER!

​
Tech Stack
Python 3.x
Built-in random module for computer moves