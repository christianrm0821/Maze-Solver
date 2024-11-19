# Maze Solver

A Python project using `tkinter` to visualize and solve mazes using the Depth-First Search (DFS) algorithm. The application generates a random maze and solves it step-by-step, showing the solution path.

---

## Features

- **Maze Visualization**: A grid-based maze is displayed on the screen.
- **Depth-First Search**: The algorithm traverses the maze to find a solution.
- **Interactive GUI**: Built with `tkinter`, making it lightweight and functional

# How It Works

## Maze Generation
The program initializes a grid and generates a maze displayed as a visual representation using the Canvas widget from tkinter.
![image](https://github.com/user-attachments/assets/5f814f3b-57ca-402c-b792-4fe24f2cc3bd)


## Maze Solving with DFS
Depth-First Search (DFS):
  Starts at the maze's entry point.
  Explores all paths recursively until reaching the exit.
  Marks visited nodes to avoid revisiting.
  Backtracks when necessary to find the correct path.
  The solution path is dynamically drawn on the canvas, showing how DFS navigates through the maze.

![image](https://github.com/user-attachments/assets/6ae04b83-3029-4172-ad6b-2312dab6ac6d)



