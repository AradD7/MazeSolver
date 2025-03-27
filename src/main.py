from line import Line
from point import Point
from window import Window

window_width = 1920
window_height = 1080


def main():
    win = Window(window_width, window_height)
    test_line = Line(Point(300, 300), Point(500, 300))
    win.draw_line(test_line, "red")
    win.wait_for_close()


main()
