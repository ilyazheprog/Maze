import pygame
from pygame.locals import *

from window import root
from config import *

# пока круг
class Player:
    def __init__(self, color, r, pos):
        self.color = color
        self.r = r
        self.cur_pos = pos
        self.prev_pos = None
        self.score = 0

    def draw(self):
        pygame.draw.circle(root.screen, self.color, self.cur_pos, self.r)

    def move(self):
        x, y = self.cur_pos
        self.prev_pos = self.cur_pos
        if pygame.key.get_pressed()[K_LEFT] and x - R - SPEED >= 0:
            x -= SPEED

        if pygame.key.get_pressed()[K_RIGHT] and x + R + SPEED <= W:
            x += SPEED

        if pygame.key.get_pressed()[K_UP] and y - R - SPEED >= 0:
            y -= SPEED

        if pygame.key.get_pressed()[K_DOWN] and y + R + SPEED <= H:
            y += SPEED

        self.cur_pos = x, y

    def collider(self):
        x, y = self.cur_pos
        return pygame.Rect(x - self.r, y - self.r, 2 * self.r-5, 2 * self.r-5)


player = Player(COLORPL, R, (22, 28))
