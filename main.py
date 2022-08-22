import pygame

from random import randint

from src.config import *
from src.window import root
from src.player import player
from src.text import Text
from src.exp import exp, Exp
from src.maze import maze
from src.floor import fl

clock = pygame.time.Clock()

while 1:
    root.fill(WHITE)
    maze.build()

    player.draw()

    fl.draw()
    player.move()

    root.update()

    clock.tick(FPS)
    pygame.event.pump()

    root.listen()