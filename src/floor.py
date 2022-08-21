import pygame

from .config import *
from .cell import Cell


class Floor:
    def __init__(self):
        self.floor = [[Cell((i, j), CELL_W, CELL_H) for i in range(0, W, CELL_W+BORDER)]
                      for j in range(0, H, CELL_H+BORDER)]
        w, h = len(self.floor[0]), len(self.floor)
        for i in range(h):
            for j in range(w):
                if i == 0:
                    self.floor[i][j].is_up_border = True
                elif i == h - 2:
                    self.floor[i][j].is_bottom_border = True

                if j == 0:
                    self.floor[i][j].is_left_border = True
                elif j == w - 2:
                    self.floor[i][j].is_right_border = True

    def draw(self):
        for row in self.floor:
            for c in row:
                c.draw()

    def __getitem__(self, item):
        return self.floor[item // COUNT_CELL_VERTICAL][item % COUNT_CELL_HORIZONTAL]

    def get_num_from_pos(self, pos):
        num = None
        for i in range(COUNT_CELL_VERTICAL):
            for j in range(COUNT_CELL_HORIZONTAL):
                if self.floor[i][j] == pos:
                    index = i, j
                    break
        return num


fl = Floor()
