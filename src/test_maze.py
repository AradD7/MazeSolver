import unittest
from maze import Maze
from point import Point

class test_maze(unittest.TestCase):
    def test_maze1(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_reset(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        

        for i in range(m1._num_columns):
            for j in range(m1._num_rows):
                self.assertEqual(
                    m1._cells[i][j].visited,
                    False,
                )

