import pygame
from pygame.locals import *

from .player import player
from .text import Text
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
        paused = Text("Paused", "Arial", H // 5)
        paused.draw(root.screen, W // 4, H // 10)
        score = Text(f"Current score: {player.score}", "Arial", H // 9, GREEN)
        score.draw(root.screen, W // 5, H // 3 + 80)

        menu=ButtonMenu("To menu", (W//3+40,H-H//15-40), H//15, "violet")

        button_continue_unfocused.show(root)
        menu.show(root)
        while True:
            menu=menu.have_focus()
            menu.show(root)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                    root.exit()
                elif button_continue_unfocused.click(event, root) or pygame.key.get_pressed()[K_ESCAPE]:
                    game.run(root)
                elif menu.click(event, root):
                    main_menu.run(root)

            pygame.display.update()
            game.clock.tick(15)


pause = PauseMode()
