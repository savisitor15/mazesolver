from gui import Point, Cell, Colors, Window
import time
import random

class Maze(object):
    def __init__(self, x1:float, y1:float, num_rows:int, num_cols:int, cell_size_x:float, cell_size_y:float, win:Window = None, seed:int = None):
        self._origin = Point(x1, y1)
        self._rows = num_rows
        self._cols = num_cols
        self._cell_size = Point(cell_size_x, cell_size_y)
        self._win = win
        self._cells = []
        self._seed = seed
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for x in range(self._cols):
            row_list = []
            for y in range(self._rows):
                cell_origin = self._origin + Point(x * self._cell_size.x, y * self._cell_size.y)
                cell_tip = self._origin + Point((x + 1) * self._cell_size.x, (y+1) * self._cell_size.y)
                row_list.append(Cell(cell_origin, cell_tip, self._win))
            self._cells.append(row_list)
        for i, col in enumerate(self._cells):
            for j, row in enumerate(col):
                self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        if not self._cells:
            return
        maze_entrance:Cell = self._cells[0][0]
        maze_entrance.has_left_wall = False
        self._draw_cell(0,0)
        maze_exit:Cell = self._cells[self._cols-1][self._rows-1]
        maze_exit.has_bottom_wall = False
        self._draw_cell(self._cols-1, self._rows-1)

    def _break_walls_r(self, i, j):
        if not self._cells:
            return
        cell:Cell = self._cells[i][j]
        cell.visited = True
        while True:
            to_visit = []
            if i+1 < len(self._cells) and not self._cells[i+1][j].visited:
                to_visit.append((i+1,j))
            if j+1 < len(self._cells[i]) and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1,j))
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i,j-1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            direction = random.choice(to_visit)
            if direction[0] > i: #Right
                cell.has_right_wall = False
                self._cells[direction[0]][direction[1]].has_left_wall = False
            if direction[0] < i: #Left
                cell.has_left_wall = False
                self._cells[direction[0]][direction[1]].has_right_wall = False
            if direction[1] > j: #Down
                cell.has_bottom_wall = False
                self._cells[direction[0]][direction[1]].has_top_wall = False
            if direction[1] < j: #Up
                cell.has_top_wall = False
                self._cells[direction[0]][direction[1]].has_bottom_wall = False
            self._break_walls_r(direction[0], direction[1])

    def _reset_cells_visited(self):
        for i in self._cells:
            for j in i:
                j.visited = False


    def _draw_cell(self, i, j):
        cell:Cell = self._cells[i][j]
        cell.draw(Colors.BLACK)
        self._animate()
    
    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        time.sleep(0.01)

