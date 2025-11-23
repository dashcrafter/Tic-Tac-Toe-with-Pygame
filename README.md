# Tic Tac Toe – Python / Pygame

This project is a complete **Tic Tac Toe game** written in **Python** using **Pygame**.
It uses separate files for game logic, rendering (GUI), and configuration.
Custom PNG assets (board, X, O) are included.

---

## How to Run

### Install Python
[Install Python here](https://www.python.org/downloads/)

### Install Pygame
```bash
pip install pygame
```
### Start the Game
```bash
python gameplay.py
```
A game window will open where you can click on tiles to place X or O.

---

## File Details

### game.py
Handles:
- Game state
- Switching players
- Move validation
- Winner detection
- Draw detection
- Reset

### Start.py
Handles:
- Pygame window
- Drawing the board and symbols
- Mouse input
- Displaying winner/draw messages
- Reset after the game ends

### config.py
Defines:
- Window width/height
- Cell size
- FPS

---

## 📦 Requirements

- Python 3.x
- Pygame
