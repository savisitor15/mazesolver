from gui import Point, Cell, Colors, Window
import time

class Maze(object):
    def __init__(self, x1:float, y1:float, num_rows:int, num_cols:int, cell_size_x:float, cell_size_y:float, win:Window = None):
        self._origin = Point(x1, y1)
        self._rows = num_rows
        self._cols = num_cols
        self._cell_size = Point(cell_size_x, cell_size_y)
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()

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
        maze_entrance:Cell = self._cells[0][0]
        maze_entrance.has_left_wall = False
        self._draw_cell(0,0)
        maze_exit:Cell = self._cells[self._cols-1][self._rows-1]
        maze_exit.has_bottom_wall = False
        self._draw_cell(self._cols-1, self._rows-1)
        
    
    def _draw_cell(self, i, j):
        cell:Cell = self._cells[i][j]
        cell.draw(Colors.BLACK)
        self._animate()
    
    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        time.sleep(0.05)

