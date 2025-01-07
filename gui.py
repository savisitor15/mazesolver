from tkinter import Tk, BOTH, Canvas
from enum import Enum

class Colors(Enum):
    RED = "red"
    BLACK = "black"

class Window(object):
    def __init__(self, width, height, root=None, title="maze solver") -> 'Window':
        self.__root = Tk() if not root else root
        self.__root.title = title
        self.__canvas = Canvas()
        self.__canvas.pack(expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line:'Line', fillcolor:Colors):
        line.draw(self.__canvas, fillcolor)

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self) -> None:
        self.__running = False


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line(object):
    def __init__(self, pointA:Point, pointB:Point):
        self.__start = pointA
        self.__end = pointB
    
    def draw(self, canvas:Canvas, fillcolor:Colors):
        if fillcolor not in Colors:
            raise ValueError("Invalid color!")
        canvas.create_line(self.__start.x, self.__start.y, self.__end.x, self.__end.y,
                           fill=fillcolor.value)
        
class Cell(object):
    def __init__(self, tleft:Point, bright:Point):
        self.__x1 = tleft.x
        self.__y1 = tleft.y
        self.__x2 = bright.x
        self.__y2 = bright.y
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self.has_right_wall = True

    def draw(self, canvas:Canvas, fillcolor:Colors):
        if fillcolor not in Colors:
            raise ValueError("Invalid color!")
        fillcolor = fillcolor.value
        if self.has_top_wall:
            canvas.create_line(self.__x1, self.__y1, self.__x2, self.__y1, fill=fillcolor)
        if self.has_bottom_wall:
            canvas.create_line(self.__x1, self.__y2, self.__x2, self.__y2, fill=fillcolor)
        if self.has_left_wall:
            canvas.create_line(self.__x1, self.__y1, self.__x1, self.__y2, fill=fillcolor)
        if self.has_right_wall:
            canvas.create_line(self.__x2, self.__y1, self.__x2, self.__y2, fill=fillcolor)

