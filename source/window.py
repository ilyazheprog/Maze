from game_engine.window import Window
from config import W, H, rewrite, global_settings
from player import player
from text import cur_score_in_game
from pause_mode import pause


import pygame
from pygame.locals import *
import sys


class RootWin(Window):
    def __init__(self, size, capture):
        super().__init__(size, capture)

    @staticmethod
    def exit():
        rewrite(global_settings)
        pygame.quit()
        sys.exit()

    def listen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.WINDOWMINIMIZED or pygame.key.get_pressed()[K_ESCAPE]:
                pause.run(root)

        if pygame.key.get_pressed()[K_q]:
            self.exit()

        if pygame.key.get_pressed()[K_s] and not self._score_visible:
            self._score_visible = True
        elif pygame.key.get_pressed()[K_s] and self._score_visible:
            self._score_visible = False

        if self._score_visible:
            cur_score_in_game.set_text(f"Score: {player.score}")
            cur_score_in_game.draw(self._screen)


root = RootWin((W, H), "Maze")
