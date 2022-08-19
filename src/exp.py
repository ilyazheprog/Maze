import pygame

from .window import root
from .config import EXP


class Exp(pygame.sprite.Sprite):
    def __init__(self, pos, color=EXP, r=20, *groups):
        super().__init__(*groups)
        self.color = color
        self.r = r
        self.pos = pos

    def draw(self):
        x, y = self.pos
        pygame.draw.circle(root.screen, self.color, (x + self.r, y + self.r), self.r)
    def collider(self):
        x, y = self.pos
        return pygame.Rect(x-self.r, y-self.r, 2*self.r, 2*self.r)

    def is_touched(self, pl):
        return self.collider().colliderect(pl.collider())
