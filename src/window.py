import pygame
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


root = Window((W, H))
