import pygame
from pygame.locals import *

import sys

from .config import *
from .player import player
from .text import Text


class Window:
    def __init__(self, size):
        pygame.init()
        self.score_visiblle = False
        self.screen = pygame.display.set_mode(size)
        self.score = None

    def exit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        pygame.display.update()

    def fill(self, color):
        self.screen.fill(color)

    def listen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()

        if pygame.key.get_pressed()[K_q]:
            self.exit()

        if pygame.key.get_pressed()[K_s] and not self.score_visiblle:
            self.score_visiblle = True
        elif pygame.key.get_pressed()[K_s] and self.score_visiblle:
            self.score_visiblle = False

        if self.score_visiblle:
            self.score = Text(f"Score: {player.score}", "Arial", 40)
            self.score.draw(self.screen, W//2-50, H//2-50)


root = Window((W, H))
