import pygame

from src.config_color import WHITE, GREEN
from src.config import FPS, W, H
from src.player import player
from src.maze import maze


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

    def run(self, root):
        root.set_capture("Maze")

        while 1:
            root.fill(WHITE)
            maze.build(root.screen)

            player.show(root.screen)

            player.move()

            root.listen()
            root.update()

            self.clock.tick(FPS)
            pygame.event.pump()


game = Game()
