import pygame

from window import root
from config import *


class Cell:
    def __init__(self, pos, w, h):
        self.pos = pos
        self.w = w
        self.h = h
        self.cell = pygame.Rect(*self.pos, self.w, self.h)

    def draw(self):
        pygame.draw.rect(root.screen, width=BORDER, color=(0, 0, 0), rect=self.cell)