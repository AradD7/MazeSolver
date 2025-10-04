from maze import Maze
from point import Point
from window import Window


window_width = 3072
window_height = 1620
full_screen = True


def main():
    win = Window(window_width, window_height, full_screen)
    the_maze = Maze(Point(50, 50), 28, 45, 60, 60, win)

    the_maze.solve()


    win.wait_for_close()


main()
