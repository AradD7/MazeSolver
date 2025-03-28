from line import Line
from point import Point
from window import Window

class Cell():
    def __init__(self, win: Window):
        self._p1 = Point(0, 0)
        self._p2 = Point(0, 0)
        self.has_left_wall = True
        self.has_top_wall= True
        self.has_right_wall = True 
        self.has_bottom_wall = True 
        self.__win = win

    def draw(self, p1: Point, p2: Point, fill_color="black"):
        self._p1 = p1
        self._p2 = p2
        top_left = Point(self._p1.x, self._p1.y)
        top_right = Point(self._p2.x, self._p1.y)
        bottom_right = Point(self._p2.x, self._p2.y)
        bottom_left = Point(self._p1.x, self._p2.y)

        if self.has_left_wall:
            self.__win.draw_line(Line(top_left, bottom_left), fill_color)
        if self.has_top_wall:
            self.__win.draw_line(Line(top_left, top_right), fill_color)
        if self.has_right_wall:
            self.__win.draw_line(Line(top_right, bottom_right), fill_color)
        if self.has_bottom_wall:
            self.__win.draw_line(Line(bottom_left, bottom_right), fill_color)

    def draw_move(self, to_cell, undo=False):
        c1 = Point((self._p1.x + self._p2.x) // 2, (self._p1.y + self._p2.y) // 2)
        c2 = Point((to_cell._p1.x + to_cell._p2.x) // 2, (to_cell._p1.y + to_cell._p2.y) // 2)

        if undo:
            self.__win.draw_line(Line(c1, c2), fill_color="gray")
        if not(undo):
            self.__win.draw_line(Line(c1, c2), fill_color="red")






