import pygame
from pygame.locals import *

import sys
from json import dump

from .config import *
from .player import player
from .text import cur_score_in_game
from .pause_mode import pause


class Window:
    def __init__(self, size, capture):
        self.__score_visible = False
        self.__display = pygame.display
        self.__screen = self.__display.set_mode(size)
        self.__capture = capture
        self.__score = None
        self.__minimized = False

    @property
    def screen(self):
        return self.__screen

    @staticmethod
    def exit():
        with open("src/config.json", "w") as f:
            f.write(dumps(global_settings, indent=4))
        pygame.quit()
        sys.exit()

    def update(self):
        self.__display.update()

    def fill(self, color=None, img=None):
        if color is not None:
            self.screen.fill(color)
        else:
            self.screen.blit(img, (0, 0))

    def set_capture(self, capture):
        self.__display.set_caption(capture)

    def listen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.WINDOWMINIMIZED or pygame.key.get_pressed()[K_ESCAPE]:
                pause.run(root)

        if pygame.key.get_pressed()[K_q]:
            self.exit()

        if pygame.key.get_pressed()[K_s] and not self.__score_visible:
            self.__score_visible = True
        elif pygame.key.get_pressed()[K_s] and self.__score_visible:
            self.__score_visible = False

        if self.__score_visible:
            cur_score_in_game.set_text(f"Score: {player.score}")
            cur_score_in_game.show(self.__screen)


root = Window((W, H), "Maze")
