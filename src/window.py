from tkinter import Tk, Canvas, BOTH
from line import Line

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__cavas = Canvas(self.__root, {"height": height, "width": width})
        self.__cavas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def draw_line(self, line: Line, fill_color):
        line.draw(self.__cavas, fill_color)

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed :(")

    def close(self):
        self.__running = False

