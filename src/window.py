import pygame
from pygame.locals import *

import sys
from time import sleep

from .config import *
from .player import player
from .text import Text
from .game import game

class Window:
    def __init__(self, size, capture):
        self.__score_visible = False
        self.__screen = pygame.display.set_mode(size)
        self.__capture = capture
        self.__score = None
        self.__minimized = False

    @property
    def screen(self):
        return self.__screen

    @staticmethod
    def exit():
        pygame.quit()
        sys.exit()

    @staticmethod
    def update():
        pygame.display.update()

    def fill(self, color=None, img=None):
        if color is not None:
            self.screen.fill(color)
        else:
            self.screen.blit(img, (0, 0))

    def set_capture(self, capture):
        pygame.display.set_caption(capture)

    def listen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.WINDOWMINIMIZED or pygame.key.get_pressed()[K_ESCAPE]:
                game.pause(root)

        if pygame.key.get_pressed()[K_q]:
            self.exit()

        if pygame.key.get_pressed()[K_s] and not self.__score_visible:
            self.__score_visible = True
        elif pygame.key.get_pressed()[K_s] and self.__score_visible:
            self.__score_visible = False

        if self.__score_visible:
            self.__score = Text(f"Score: {player.score}", "Arial", 40)
            self.__score.draw(self.__screen, W // 2 - 50, H // 2 - 50)


root = Window((W, H), "Maze")
