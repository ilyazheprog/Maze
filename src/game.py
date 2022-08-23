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
        bg = pygame.image.load("resources/images/pause background.png")
        root.fill(img=bg)
        root.set_capture("Maze [paused]")
        paused = Text("Paused", "Arial", 200)
        paused.draw(root.screen, 87, 50)
        score = Text(f"Current score: {player.score}", "Arial", 90, GREEN)
        score.draw(root.screen, 87, 300)

        button = Button("       Continue        ", (89, 550), font=80, bg="navy")
        button.show(root)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                    root.exit()
                elif button.click(event) or pygame.key.get_pressed()[K_ESCAPE]:
                    self.run(root)

            pygame.display.update()
            self.clock.tick(15)


game = Game()
