# Labyrinth Game

Welcome to Labyrinth Game! I’ve been developing this board game concept during my weekends. I am creating a digital prototype to test the gameplay mechanics. I plan to bring it to life as a physical board game if it proves successful.

This interactive board game is implemented in Python using the Pygame library. Players take on the roles of Runners and Chasers, navigating a labyrinth filled with challenges and strategic card plays.

## Table of Contents

- [Game Overview](#game-overview)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Rules](#game-rules)
- [Contributing](#contributing)


## Game Overview

In the Labyrinth Game, two players compete against each other: the Runner trying to escape through the exit and the Chaser trying to catch the Runner. Players use cards to move, manipulate the board, and strategize their way through the labyrinth.

## Features

- Interactive gameplay with Pygame.
- Various types of cards that provide different actions:
  - Movement Cards
  - Key Cards
  - Rotate Cards
  - Draw Cards
  - Switch Places Cards
- A dynamic labyrinth that players navigate.
- Simple terminal-based input for selecting cards and directions.

## Installation

To run the Labyrinth Game, you must install Python and Pygame using pip. Follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/labyrinth-game.git
   cd labyrinth-game

## How to Play
- Start the Game: Run the main_game.py file.
- Select Your Card: Each player selects a card from their hand.
- Choose a Direction: After selecting a card, choose a direction to move (up, down, left, right).
- Use Card Effects: Perform the corresponding action depending on the card type.
- Win Conditions:
  - The Runner wins by reaching the exit.
  - The Chaser wins by catching the Runner.

## Game Rules
- The game board is a 10x10 grid, where:
     - The blue circle represents the Runner.
     - The red circle represents the Chaser.
     - The green box represents the exit.
     - The white tiles represent walls.
     - The hollow walkway represents open spaces.
- Players can use cards to move, manipulate the board, or draw new cards.
- Players can only move through walls if they use a Key Card.
- The game ends when the Runner escapes or the Chaser catches the Runner.

## Contributing
- Contributions are welcome! If you have suggestions for improvements or features, open an issue or submit a pull request.
    - Fork the repository.
    - Create a new branch (git checkout -b feature/YourFeature).
    - Make and commit your changes (git commit -m 'Add some feature').
    - Push to the branch (git push origin feature/YourFeature).
    - Open a pull request.

