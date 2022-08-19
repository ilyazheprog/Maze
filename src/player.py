import pygame
from pygame.locals import *

from time import sleep

from .window import root
from .config import *
from .sounds import crashing


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
        sleep(.045)
        if pygame.key.get_pressed()[K_LEFT]:
            if x - 2*R >=0:
                x -= 2*R
            else:
                crashing.play()
        elif pygame.key.get_pressed()[K_RIGHT]:
            if x + 2*R < W:
                x += 2*R
            else:
                crashing.play()
        elif pygame.key.get_pressed()[K_UP]:
            if y - 2*R >=0:
                y -= 2*R
            else:
                crashing.play()
        elif pygame.key.get_pressed()[K_DOWN]:
            if y + 2*R <= H:
                y += 2*R
            else:
                crashing.play()

        self.cur_pos = x, y

    def collider(self):
        x, y = self.cur_pos
        return pygame.Rect(x - self.r, y - self.r, CELL_W, CELL_H)


player = Player(COLOR_FOR_PLAYER, R, (R, R))
