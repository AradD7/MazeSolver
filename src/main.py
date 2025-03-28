from cell import Cell
from point import Point
from window import Window


window_width = 1920
window_height = 1080


def main():
    win = Window(window_width, window_height)
    test_cell1 = Cell(win)
    test_cell1.has_right_wall = False
    test_cell1.draw(Point(100, 100), Point(200, 200))

    test_cell2 = Cell(win)
    test_cell2.has_left_wall = False
    test_cell2.draw(Point(220, 100), Point(320, 200))

    test_cell1.draw_move(test_cell2, True)

    win.wait_for_close()


main()
