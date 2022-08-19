import pygame
from pygame.locals import *
from time import sleep
from random import randint
from config import *
from window import root
from player import player
from text import Text
from exp import Exp
from wall import Wall
from maze import Maze
from cell import Cell
from floor import fl

clock = pygame.time.Clock()
maze = Maze()

collect = pygame.mixer.Sound('src/sounds/collected.mp3')

e=[Exp((randint(96, 1000), randint(96, 600-33+1))) for _ in range(10)]
while 1:
    root.fill(WHITE)
    fl.draw()
    '''
    t=Text(f"Score: {player.score}", 'serif', 20)
    t.draw((1100,  20))
    if not len(e):
        maze = Maze()
        e = [Exp((randint(96, 1000), randint(98, 600 -33 + 1))) for _ in range(10)]
        player.cur_pos = (30, 50)
        
    maze.build()'''

    player.draw()

    '''for o in e:
        o.draw()
        if o.is_touched(player):
            player.score+=1
            collect.play()
            e.remove(o)

    for w in maze.walls:
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