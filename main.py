import pygame
from pygame.locals import *
from random import choice

from src.config import *
from src.window import root
from src.player import player
from src.text import Text
from src.exp import Exp
from src.maze import Maze
from src.floor import fl
from src.sounds import collect

clock = pygame.time.Clock()
maze = Maze()
lups = [c.pos for r in fl.floor for c in r]


e=[Exp(choice(lups)) for _ in range(10)]
while 1:
    root.fill(WHITE)
    #maze.build()

    player.draw()

    for o in e:
        o.draw()
        if o.is_touched(player):
            player.score+=1
            collect.play()
            e.remove(o)
    fl.draw()

    t=Text(f"Score: {player.score}", 'serif', 20)
    t.draw((1100,  20))
    if not len(e):
        #maze = Maze()
        #e = [Exp()) for _ in range(10)]
        player.cur_pos = (30, 50)


    '''for w in maze.walls:
        if w.touch(player):
            player.cur_pos=player.prev_pos'''

    player.move()

    root.update()

    clock.tick(FPS)
    pygame.event.pump()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            root.exit()

    if pygame.key.get_pressed()[K_r]:
        maze = Maze()