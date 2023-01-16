import pygame

from floor import fl
from config import CELL_H, CELL_W


class Wall:
    def __init__(self, cell):
        self.cell = cell
        fl[self.cell].is_wall = True

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(*fl[self.cell].pos, CELL_W, CELL_H))
