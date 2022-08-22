import pygame
from pygame.locals import *

import sys

from .config import *


class Window:
    def __init__(self, size):
        pygame.init()
        self.screen = pygame.display.set_mode(size)

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
                root.exit()

        if pygame.key.get_pressed()[K_q]:
            root.exit()


root = Window((W, H))
