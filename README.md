# Maze Solver

A Python-based maze generator and solver with real-time visualization using Tkinter. Watch as mazes are procedurally generated and then solved with animated pathfinding.

## Features

- **Procedural Maze Generation** - Uses recursive backtracking algorithm to create unique, solvable mazes
- **Automated Solving** - Implements depth-first search with visual backtracking
- **Real-time Visualization** - Animated maze generation and solving process
- **Customizable Parameters** - Configurable maze size, cell dimensions, and window settings
- **Fullscreen Support** - Optional fullscreen mode for immersive visualization
- **Path Visualization** - Red lines show the current path, gray lines show backtracking

## Requirements

- Python 3.x
- tkinter (usually included with Python)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/maze-solver.git
cd maze-solver
```

2. Make the shell scripts executable (if needed):
```bash
chmod +x main.sh test.sh
```

3. Run the maze solver:
```bash
./main.sh
```

Or manually:
```bash
python3 src/main.py
```

## Usage

### Basic Usage

Run the provided shell script to generate and solve a maze with default settings:

```bash
./main.sh
```

### Customization

Edit the parameters in `src/main.py` to customize the maze:

```python
window_width = 3072      # Window width in pixels
window_height = 1620     # Window height in pixels
full_screen = True       # Enable fullscreen mode

# Maze parameters
the_maze = Maze(
    Point(50, 50),  # Starting position (x, y)
    28,             # Number of rows
    45,             # Number of columns
    60,             # Cell width
    60,             # Cell height
    win
)
```

## How It Works

### Maze Generation
The maze is generated using a **recursive backtracking algorithm**:
1. Start at the top-left cell
2. Mark the current cell as visited
3. Randomly choose an unvisited neighbor
4. Remove the wall between the current cell and chosen neighbor
5. Recursively visit the chosen neighbor
6. Backtrack when no unvisited neighbors remain

### Maze Solving
The solver uses a **depth-first search (DFS)** algorithm:
1. Start at the top-left cell (entrance)
2. Mark current cell as visited
3. Try moving to unvisited neighbors through open walls
4. Draw the path in red as it explores
5. If a dead end is reached, backtrack (shown in gray)
6. Continue until the bottom-right cell (exit) is found

## Project Structure

```
maze-solver/
├── README.md
├── main.sh           # Script to run the maze solver
├── test.sh           # Script to run unit tests
└── src/
    ├── main.py       # Entry point
    ├── maze.py       # Maze generation and solving logic
    ├── cell.py       # Cell class with wall properties
    ├── window.py     # Tkinter window wrapper
    ├── line.py       # Line drawing utilities
    ├── point.py      # Point coordinate class
    └── test_maze.py  # Unit tests
```

## Testing

Run the unit tests using the provided script:

```bash
./test.sh
```

Or manually:
```bash
python3 -m unittest discover -s src
```

## Controls

- Close the window or press `Ctrl+C` to exit

## Screenshots

<p align="center">
  <img src="screenshot/MazeSolver-1.png" width="45%" />
  <img src="screenshot/MazeSolver-2.png" width="45%" />
</p>

---

<sub>Despite being based on a Boot.dev guided project, 100% of the code is written by me</sub>
