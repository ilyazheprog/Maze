import pygame
from pygame.locals import *

from .text import Text
from .config import *
from .button import button_start_unfocused, button_settings_unfocused
from .game import game
from .settings import settings


class MainMenu:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.bg = BACKGROUND_IMAGE_OBJ

    def run(self, root):
        root.fill(img=self.bg)
        root.set_capture("Maze [menu]")
        paused = Text("Menu", "Arial", H // 8)
        paused.draw(root.screen, W // 4 + W // 9, H // 10)

        button_start_unfocused.show(root)
        button_settings_unfocused.show(root)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                    root.exit()
                elif button_start_unfocused.click(event, root) or pygame.key.get_pressed()[K_ESCAPE]:
                    game.run(root)
                elif button_settings_unfocused.click(event, root):
                    settings.run(root)

            pygame.display.update()
            self.clock.tick(15)


main_menu = MainMenu()
