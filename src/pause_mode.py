import pygame
from pygame.locals import *

from .player import player
from .text import cur_score_in_pause, paused
from .button import *
from .config import *
from .game import game
from .main_menu import main_menu


class PauseMode:
    def __init__(self):
        self.bg = BACKGROUND_IMAGE_OBJ
    
    def run(self, root):
        root.set_capture("Maze [paused]")
        root.fill(img=self.bg)

        paused.show(root.screen)

        cur_score_in_pause.set_text(f"Current score: {player.score}")
        cur_score_in_pause.show(root.screen)

        # Draw buttons
        button_continue.show(root)
        button_menu.show(root)

        while True:
            # Change button color on hover
            button_menu.manage_focus()
            button_continue.manage_focus()

            # Re-show buttons
            button_menu.show(root)
            button_continue.show(root)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                    root.exit()

                # Handling clicks
                elif button_continue.click(event) or pygame.key.get_pressed()[K_ESCAPE]:
                    game.run(root)
                elif button_menu.click(event):
                    main_menu.run(root)

            pygame.display.update()
            game.clock.tick(15)


pause = PauseMode()
