import pygame

from .config_color import WHITE, GREEN
from .config import FPS, W, H
from .player import player
from .maze import maze


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


game = Game()
