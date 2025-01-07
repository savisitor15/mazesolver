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
