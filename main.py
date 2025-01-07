from gui import Window
from maze import Maze

if __name__ == "__main__":
    win = Window(620, 620)
    maze = Maze(10, 10, 30, 30, 20, 20, win)
    win.wait_for_close()
