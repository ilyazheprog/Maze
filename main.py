import pygame
from pygame.locals import *
from random import randint

from src.config import *
from src.window import root
from src.player import player
from src.text import Text
from src.exp import exp
from src.maze import Maze
from src.floor import fl

clock = pygame.time.Clock()
maze = Maze()

while 1:
    root.fill(WHITE)
    maze.build()

    player.draw()

    for o in exp:
        if o is None:
            continue
        o.draw()

    fl.draw()
    player.move()

    root.update()

    clock.tick(FPS)
    pygame.event.pump()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            root.exit()

    if pygame.key.get_pressed()[K_r]:
        maze = Maze()
    if pygame.key.get_pressed()[K_q]:
        root.exit()