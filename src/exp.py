import pygame

from .window import root
from .config import EXP, R


class Exp(pygame.sprite.Sprite):
    def __init__(self, pos, color=EXP, r=R, *groups):
        super().__init__(*groups)
        self.color = color
        self.r = r
        self.pos = pos

    def draw(self):
        x, y = self.pos
        pygame.draw.circle(root.screen, self.color, (x + self.r, y + self.r), self.r)
    def collider(self):
        x, y = self.pos
        return pygame.Rect(x-self.r, y-self.r, 1, 1)

    def is_touched(self, pl):
        return self.collider().center == pl.center
