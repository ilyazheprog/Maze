import pygame

from random import randint

from src.config import *
from src.window import root
from src.player import player
from src.maze import maze

def main():
    pygame.init()
    clock = pygame.time.Clock()

    while 1:
        root.fill(WHITE)
        maze.build(root.screen)

        player.draw(root.screen)

        player.move()

        root.listen()
        root.update()

        clock.tick(FPS)
        pygame.event.pump()


if __name__ == "__main__":
    main()
