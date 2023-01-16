import pygame
from random import randint


from floor import fl
from config import *


exp = [None for _ in range(COUNT_CELL_HORIZONTAL**2)]


class Exp:
    def __init__(self, cell, color=EXP):
        self.__color = color
        self.__cell = cell
        
    def generate(self):
        for _ in range(10):
            cell = randint(1, COUNT_CELL_VERTICAL**2-1)
        
            while fl[cell].is_wall:
                cell = randint(1, COUNT_CELL_VERTICAL ** 2 - 1)
        
            fl[cell].is_exp = True
            exp[cell] = Exp(cell)

    def draw(self, surface):
        x, y = fl[self.__cell].pos
        pygame.draw.circle(surface, self.__color, (x + R, y + R), R)


