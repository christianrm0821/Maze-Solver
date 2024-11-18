import unittest
from Maze import Maze
from Window import *

class Tests(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()
