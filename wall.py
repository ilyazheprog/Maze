import pygame

from window import root


class Wall:
    def __init__(self, left_up_point, w, h):
        self.lup = left_up_point
        self.w = w
        self.h = h
        self.wall = self.collider()

    def draw(self):
        pygame.draw.rect(root.screen, (0, 0, 0), self.wall)

    def collider(self):
        return pygame.Rect(*self.lup, self.w, self.h)

    def touch(self, player):
        return self.wall.colliderect(player.collider())
