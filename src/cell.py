import pygame

from .window import root
from .config import *


class Cell:
    def __init__(self, pos, w, h, is_left_border=False, is_up_border=False, is_right_border=False,
                 is_bottom_border=False, is_exp=False, is_wall=False):
        self.pos = pos[0] + BORDER, pos[1] + BORDER
        self.w = w
        self.h = h
        self.is_left_border = is_left_border
        self.is_up_border = is_up_border
        self.is_right_border = is_right_border
        self.is_bottom_border = is_bottom_border
        self.is_exp = is_exp
        self.is_wall = is_wall
        self.cell = pygame.Rect(*self.pos, self.w, self.h)

    def draw(self):
        pygame.draw.rect(root.screen, width=BORDER, color=(0, 0, 0), rect=self.cell)
