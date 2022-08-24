import pygame
from src.config import WHITE, FPS, W, H, GREEN

from src.player import player
from src.maze import maze
from src.button import button_continue_unfocused
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


game = Game()
