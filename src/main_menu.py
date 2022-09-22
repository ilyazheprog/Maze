import pygame
from pygame.locals import *

from .text import Text
from .config import *
from .button import button_start, button_settings
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

        # Draw buttons
        button_start.show(root)
        button_settings.show(root)
        while True:
            # Change button color on hover
            button_start.manage_focus()
            button_settings.manage_focus()

            # Re-draw buttons
            button_start.show(root)
            button_settings.show(root)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                    root.exit()

                # Handling clicks
                elif button_start.click(event) or pygame.key.get_pressed()[K_ESCAPE]:
                    game.run(root)
                elif button_settings.click(event):
                    settings.run(root)

            pygame.display.update()
            self.clock.tick(15)


main_menu = MainMenu()
