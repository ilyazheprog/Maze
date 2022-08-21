import pygame

from .window import root
from .floor import fl
from .config import *


class Wall:
    def __init__(self, cell):
        self.cell = cell
        fl[self.cell].is_wall = True

    def draw(self):
        pygame.draw.rect(root.screen, (0, 0, 0), pygame.Rect(*fl[self.cell].pos, CELL_W, CELL_H))
