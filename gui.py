from tkinter import Tk, BOTH, Canvas

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

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self) -> None:
        self.__running = False

