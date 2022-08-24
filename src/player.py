import pygame
from pygame.locals import *

from time import sleep

from .config import *
from .maze import maze
from .sounds import *
from .floor import fl


class Player:
    def __init__(self, color, r, cell):
        self.color = color
        self.r = r
        self.cell = cell
        self.score = 0

    def draw(self, surface):
        x, y = fl[self.cell].pos
        # pygame.draw.rect(root.__screen, BLUE, self.collider())
        pygame.draw.circle(surface, self.color, (x + self.r, y + self.r), self.r)

    def move(self):
        sleep(.1)
        if pygame.key.get_pressed()[K_LEFT]:
            if not fl[self.cell].is_left_border and not fl[self.cell - 1].is_wall:
                self.cell -= 1
            else:
                crashing.play()
        elif pygame.key.get_pressed()[K_RIGHT]:
            if not fl[self.cell].is_right_border and not fl[self.cell + 1].is_wall:
                self.cell += 1
            else:
                crashing.play()
        elif pygame.key.get_pressed()[K_UP]:
            if not fl[self.cell].is_up_border and not fl[self.cell - COUNT_CELL_HORIZONTAL].is_wall:
                self.cell -= COUNT_CELL_HORIZONTAL
            else:
                crashing.play()
        elif pygame.key.get_pressed()[K_DOWN]:
            if not fl[self.cell].is_bottom_border and self.cell + COUNT_CELL_HORIZONTAL < COUNT_CELL_HORIZONTAL**2 and not fl[self.cell + COUNT_CELL_HORIZONTAL].is_wall:
                self.cell += COUNT_CELL_HORIZONTAL
            else:
                print(self.cell)
                crashing.play()

        if fl[self.cell].is_exp:
            self.score += 1
            collect.play()
            maze.remove(self.cell)



player = Player(COLOR_FOR_PLAYER, R, 0)
