# Chess AI using Minimax Algorithm with Alpha-Beta Pruning

## Overview
This project is a chess AI built using Python and Pygame. The AI leverages the **Minimax algorithm** with **Alpha-Beta pruning** to make optimal moves, ensuring a challenging and dynamic opponent for human players.

The goal is to create an interactive chess game where the AI can calculate moves based on game states and predict outcomes by exploring potential moves. This project is developed as a collaboration between Kowshikan Naveendran and Adrian Ho.

## Features
- Interactive chessboard powered by Pygame.
- AI opponent using Minimax algorithm for decision-making.
- Alpha-Beta pruning for enhanced efficiency in move calculations.
- Support for human-vs-human and human-vs-AI gameplay modes.
- Clean, user-friendly graphical interface.

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.8+
- Pygame library

To install Pygame, run:
```bash
pip install pygame
```

## How It Works
1. **Minimax Algorithm**: The AI uses the Minimax algorithm to evaluate possible moves and choose the one that maximizes its advantage while minimizing the opponent's.
2. **Alpha-Beta Pruning**: This optimization reduces the number of nodes the algorithm evaluates, making it faster and more efficient.
3. **Chessboard Logic**: The game logic manages piece movements, captures, and checks for end-game conditions such as checkmate or stalemate.

## Getting Started
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/chess-ai.git
   ```
2. Navigate to the project directory:
   ```bash
   cd chess-ai
   ```
3. Run the program:
   ```bash
   python chess_game.py
   ```

## To-Do
- Complete the logic for each piece.
- Implement the Minimax algorithm.
- Implement Alpha-Beta Pruning.
- Create complex heuristics.
- Introduce a timer for each player's turn.
- Create animations for piece movements and captures.
- Create user interface using pygame.
- Enhance the user interface for a more polished visual experience.

## Contributing
TODO

## License
TODO
