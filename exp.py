import pygame

from window import root
from config import YELLOW
from player import player


class Exp(pygame.sprite.Sprite):
    def __init__(self, pos, color=YELLOW, r=15, *groups):
        super().__init__(*groups)
        self.color = color
        self.r = r
        self.pos = pos

    def draw(self):
        pygame.draw.circle(root.screen, self.color, self.pos, self.r)

    def collider(self):
        x, y = self.pos
        return pygame.Rect(x-self.r, y-self.r, 2*self.r, 2*self.r)

    def is_touched(self, pl):
        return self.collider().colliderect(pl.collider())
