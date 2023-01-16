import pygame

from config import *
from cell import Cell, next_pos


class Floor:
    def __init__(self):
        self.__it = iter(next_pos())

        self.__floor = [None] * COUNT_CELL_HORIZONTAL**2

        for i in range(COUNT_CELL_HORIZONTAL**2):
            cell = Cell(next(self.__it))
            self.__floor[i] = cell
            if i < COUNT_CELL_HORIZONTAL:
                self.__floor[i].is_up_border = True
            elif i + COUNT_CELL_HORIZONTAL >= COUNT_CELL_HORIZONTAL**2+1:
                self.__floor[i].is_bottom_border = True

            if i % COUNT_CELL_HORIZONTAL == 0:
                self.__floor[i].is_left_border = True
            elif (i + 1) % COUNT_CELL_HORIZONTAL == 0:
                self.__floor[i].is_right_border = True

    def draw(self, surface):
        for c in self.__floor:
            c.draw(surface)

    def __getitem__(self, item):
        return self.__floor[item]


fl = Floor()