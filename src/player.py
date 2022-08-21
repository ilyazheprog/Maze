import pygame
from pygame.locals import *

from time import sleep

from .window import root
from .config import *
from .sounds import *
from .floor import fl
from .exp import exp


class Player:
    def __init__(self, color, r, cell):
        self.color = color
        self.r = r
        self.cell = cell
        self.score = 0

    @property
    def center(self):
        x, y = fl[self.cell].pos
        return x + self.r, y + self.r

    def draw(self):
        x, y = fl[self.cell].pos
        # pygame.draw.rect(root.screen, BLUE, self.collider())
        pygame.draw.circle(root.screen, self.color, (x + self.r, y + self.r), self.r)

    def move(self):
        sleep(.1)
        if pygame.key.get_pressed()[K_LEFT]:
            if not fl[self.cell].is_left_border:
                self.cell -= 1
            else:
                crashing.play()
        elif pygame.key.get_pressed()[K_RIGHT]:
            if not fl[self.cell].is_right_border:
                self.cell += 1
            else:
                crashing.play()
        elif pygame.key.get_pressed()[K_UP]:
            if not fl[self.cell].is_up_border:
                self.cell -= COUNT_CELL_HORIZONTAL
            else:
                crashing.play()
        elif pygame.key.get_pressed()[K_DOWN]:
            if not fl[self.cell].is_bottom_border:
                self.cell += COUNT_CELL_HORIZONTAL
            else:
                crashing.play()

        if fl[self.cell].is_exp:
            self.score += 1
            collect.play()
            fl[self.cell].is_exp = False
            exp[self.cell] = None


player = Player(COLOR_FOR_PLAYER, R, 52)