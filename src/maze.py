from point import Point
from window import Window
from cell import Cell
import time
import random


class Maze():
    def __init__(self, p1: Point, num_rows, num_columns, cell_size_x, cell_size_y, win=None):
        self._position = p1
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cell_visited()


    def _create_cells(self):
        for i in range(self._num_columns):
            temp_column = []
            for j in range(self._num_rows):
                temp_column.append(Cell(self._win))
            self._cells.append(temp_column)

        for i in range(self._num_columns):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        added_x = i * self._cell_size_x
        added_y = j * self._cell_size_y
        top_left = Point(self._position.x + added_x, self._position.y + added_y)
        bottom_right = Point(added_x + (self._position.x + self._cell_size_x), added_y + (self._position.y + self._cell_size_y))

        self._cells[i][j].draw(top_left, bottom_right)
        self._animate()

    def _animate(self, pause=0.005):
        if self._win is not None:
            self._win.redraw()
            time.sleep(pause)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_columns - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_columns - 1, self._num_rows - 1)

    def _break_walls_r(self,i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        
        while True:
            possible_directions = []
            
            if self._num_columns > i + 1 and not(self._cells[i + 1][j].visited):
                possible_directions.append((i + 1, j))
            if i - 1 >= 0 and not(self._cells[i - 1][j].visited):
                possible_directions.append((i - 1, j))
            if self._num_rows > j + 1 and not(self._cells[i][j + 1].visited):
                possible_directions.append((i, j + 1))
            if j - 1 >= 0 and not(self._cells[i][j - 1].visited):
                possible_directions.append((i, j - 1))

            if len(possible_directions) == 0:
                return

            direction = random.randrange(1000000000)
            direction %= len(possible_directions)
            next_cell = self._cells[possible_directions[direction][0]][possible_directions[direction][1]]

            if possible_directions[direction][0] == i + 1:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            elif possible_directions[direction][0] == i - 1:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            if possible_directions[direction][1] == j + 1:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif possible_directions[direction][1] == j - 1:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            
            self._draw_cell(i, j)
            self._break_walls_r(possible_directions[direction][0], possible_directions[direction][1])

    def _reset_cell_visited(self):
        for i in range(self._num_columns):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        if current_cell == self._cells[-1][-1]:
            return True
        current_cell.visited = True

        moves = []
        if i - 1 >= 0 and not(self._cells[i - 1][j].visited) and not(current_cell.has_left_wall):
            moves.append((i-1, j))
    
        if self._num_rows > j + 1 and not(self._cells[i][j + 1].visited) and not(current_cell.has_bottom_wall):
            moves.append((i, j+1))
    
        if self._num_columns > i + 1 and not(self._cells[i + 1][j].visited) and not(current_cell.has_right_wall):
            moves.append((i+1, j))
    
        if j - 1 >= 0 and not(self._cells[i][j - 1].visited) and not(current_cell.has_top_wall):
            moves.append((i, j-1))
    
        random.shuffle(moves)
        
        for next_i, next_j in moves:
            next_cell = self._cells[next_i][next_j]
            current_cell.draw_move(next_cell)
            if self._solve_r(next_i, next_j):
                return True
            current_cell.draw_move(next_cell, undo=True)
            self._animate()
    
        return False
        

