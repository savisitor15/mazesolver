from gui import Window
from maze import Maze

if __name__ == "__main__":
    win = Window(800, 600)
    maze = Maze(10, 10, 6, 10, 20, 20, win)
    win.wait_for_close()
