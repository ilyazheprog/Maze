import pygame


from .config import *


class Cell:
    def __init__(self, pos, w=CELL_W, h=CELL_H, is_left_border=False, is_right_border=False, is_up_border=False,
                 is_bottom_border=False, is_exp=False, is_wall=False):
        self.__pos = pos[0] + BORDER, pos[1] + BORDER
        self.__w = w
        self.__h = h
        self.__is_left_border = is_left_border
        self.__is_right_border = is_right_border
        self.__is_up_border = is_up_border
        self.__is_bottom_border = is_bottom_border
        self.__is_exp = is_exp
        self.__is_wall = is_wall
        self.__cell = pygame.Rect(*self.__pos, self.__w, self.__h)

    @property
    def pos(self):
        return self.__pos

    @property
    def is_left_border(self):
        return self.__is_left_border

    @is_left_border.setter
    def is_left_border(self, value):
        self.__is_left_border = value

    @property
    def is_right_border(self):
        return self.__is_right_border

    @is_right_border.setter
    def is_right_border(self, value):
        self.__is_right_border = value

    @property
    def is_up_border(self):
        return self.__is_up_border

    @is_up_border.setter
    def is_up_border(self, value):
        self.__is_up_border = value

    @property
    def is_bottom_border(self):
        return self.__is_bottom_border

    @is_bottom_border.setter
    def is_bottom_border(self, value):
        self.__is_bottom_border = value

    @property
    def is_exp(self):
        return self.__is_exp

    @is_exp.setter
    def is_exp(self, value):
        self.__is_exp = value

    @property
    def is_wall(self):
        return self.__is_wall

    @is_wall.setter
    def is_wall(self, value):
        self.__is_wall = value

    def draw(self, surface):
        pygame.draw.rect(surface, width=BORDER, color=(0, 0, 0), rect=self.__cell)


def next_pos():
    for j in range(0, H, CELL_H + BORDER):
        for i in range(0, W, CELL_W + BORDER):
            yield i, j
