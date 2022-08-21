import pygame
from random import randint

from .window import root
from .floor import fl
from .config import *


exp = [None for _ in range(COUNT_CELL_HORIZONTAL**2)]

class Exp:
    def __init__(self, cell, color=EXP, r=R):
        self.color = color
        self.r = r
        self.cell = cell

    def draw(self):
        x, y = fl[self.cell].pos
        pygame.draw.circle(root.screen, self.color, (x + self.r, y + self.r), self.r)


for _ in range(10):
    cell = randint(1, COUNT_CELL_VERTICAL**2-1)
    if fl[cell].is_wall:
        while fl[cell].is_wall:
            cell = randint(1, COUNT_CELL_VERTICAL ** 2 - 1)
    fl[cell].is_exp = True
    exp[cell] = Exp(cell)
