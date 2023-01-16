import pygame
from pygame.locals import *

from game_engine.text import Text
from config import *
from buttons import menu_button_group
from game import game
from settings import settings


class MainMenu:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.bg = BACKGROUND_IMAGE_OBJ

    def run(self, root):
        root.fill(img=self.bg)
        root.set_capture("Maze [menu]")
        paused = Text("Menu", "Arial", H // 8, (W // 4 + W // 9, H // 10))
        paused.draw(root.screen)

        # Draw buttons
        menu_button_group.draw(root)

        while True:
            # Change button color on hover
            menu_button_group.manage_focus()

            # Re-draw buttons
            menu_button_group.draw(root)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                    root.exit()

                # Handling clicks
                elif menu_button_group["start"].click(event) or pygame.key.get_pressed()[K_ESCAPE]:
                    game.run(root)
                elif menu_button_group["settings"].click(event):
                    settings.run(root)

            pygame.display.update()
            self.clock.tick(60)


main_menu = MainMenu()
