from gui import Window, Point, Line, Colors, Cell

if __name__ == "__main__":
    win = Window(800, 600)
    test_lines = [Line(Point(10,10), Point(10,20)),
                  Line(Point(10,20), Point(20,20)),
                  Line(Point(20,20), Point(20,10)),
                  Line(Point(10,10), Point(20,10))
    ]
    for lin in test_lines:
        win.draw_line(lin, Colors.BLACK)
    win.draw_line(Cell(Point(40,40), Point(60,60)), Colors.BLACK)
    win.wait_for_close()
