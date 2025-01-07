from tkinter import Tk, BOTH, Canvas
from enum import Enum

class Colors(Enum):
    RED = "red"
    BLACK = "black"
    GRAY = "gray"
    WHITE = "#d9d9d9"

class Window(object):
    def __init__(self, width, height, root=None, title="maze solver") -> 'Window':
        self._root = Tk() if not root else root
        self._root.title = title
        self._canvas = Canvas()
        self._canvas.pack(expand=1)
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self._root.update_idletasks()
        self._root.update()

    def draw_line(self, line:'Line', fillcolor:str):
        line.draw(self._canvas, fillcolor)

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()

    def close(self) -> None:
        self._running = False


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other:'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

class Line(object):
    def __init__(self, pointA:Point, pointB:Point):
        self._start = pointA
        self._end = pointB
    
    def draw(self, canvas:Canvas, fillcolor:Colors):
        if fillcolor not in Colors:
            raise ValueError("Invalid color!")
        canvas.create_line(self._start.x, self._start.y, self._end.x, self._end.y,
                           fill=fillcolor)
        
class Cell(object):
    def __init__(self, tleft:Point, bright:Point, win:Window = None):
        self._x1 = tleft.x
        self._y1 = tleft.y
        self._x2 = bright.x
        self._y2 = bright.y
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self.has_right_wall = True
        self._win = win
        self.visited = False

    def get_center(self) -> Point:
        return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)

    def draw(self, fillcolor:Colors):
        if not self._win:
            return
        if fillcolor not in Colors:
            raise ValueError("Invalid color!")
        fillcolor = fillcolor.value
        white = Colors.WHITE.value
        self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), fillcolor if self.has_top_wall else white)
        self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), fillcolor if self.has_bottom_wall else white)
        self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), fillcolor if self.has_left_wall else white)
        self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), fillcolor if self.has_right_wall else white)

    def draw_move(self, to_cell:'Cell', undo=False):
        if not self._win:
            return
        target: Point = to_cell.get_center()
        origin: Point = self.get_center()
        fillcolor = Colors.GRAY.value if undo else Colors.RED.value 
        self._win.draw_line(Line(Point(origin.x, origin.y), Point(target.x, target.y)), fillcolor)

