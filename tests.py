import unittest
from Maze import Maze
from Window import *

class Tests(unittest.TestCase):
    '''
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        win= Window(800,600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )
        num_cols = 1
        num_rows = 1
        win= Window(800,600)
        m1 = Maze(1, 1, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )
        num_cols = 1
        num_rows = 15
        win= Window(800,600)
        m1 = Maze(1, 1, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )
        num_cols = 20
        num_rows = 1
        win= Window(800,600)
        m1 = Maze(1, 1, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )
        '''





    def test_reset_cells_visited(self):
        win= Window(800,600)
        '''
        maze = Maze(0,0,3,3,50,50, win)
        maze.break_entrance_and_exit()
        maze.break_walls_r(0,0)
        maze.reset_cells_visited()

        for row in range(len(maze.cells)):
            for col in range(len(maze.cells[row])):
                self.assertEqual(maze.cells[row][col].visited,False, f"{row}=row  {col}=col")
        '''
    
        maze = Maze(0, 0,5, 5, 10, 10, win)  # We can pass None for window since we won't draw
    
        # Manually set some cells to visited
        maze.cells[0][0].visited = True
        maze.cells[1][1].visited = True
        
        maze.reset_cells_visited()
        
        # Verify all cells are unvisited
        for row in range(len(maze.cells)):
            for col in range(len(maze.cells[row])):
                self.assertEqual(maze.cells[row][col].visited, False, f"{row}=row  {col}=col")


if __name__ == "__main__":
    unittest.main()
