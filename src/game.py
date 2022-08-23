import pygame
from pygame.locals import *

from src.config import WHITE, FPS, W, H, GREEN

from src.player import player
from src.maze import maze
from src.button import Button
from src.text import Text


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

    def run(self, root):
        root.set_capture("Maze")

        while 1:
            root.fill(WHITE)
            maze.build(root.screen)

            player.draw(root.screen)

            player.move()

            root.listen()
            root.update()

            self.clock.tick(FPS)
            pygame.event.pump()

    def pause(self, root):
        root.fill(WHITE)
        root.set_capture("Maze [paused]")
        button = Button("Continue", (W // 3, H // 2 - 50), font=80, bg="navy")
        button.show(root)
        paused = Text("Paused", "Arial", 100)
        paused.draw(root.screen, W//3, H//10)
        score = Text(f"Current score: {player.score}", "Arial", 50, GREEN)
        score.draw(root.screen, W//3-10, H//10+140)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                    root.exit()
                elif button.click(event) or pygame.key.get_pressed()[K_ESCAPE]:
                    self.run(root)

            pygame.display.update()
            self.clock.tick(15)


game = Game()
