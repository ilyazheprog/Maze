import pygame

from random import randint

from .config import *
from .wall import Wall


class Maze:
    def __init__(self):
        self.walls = [Wall(randint(1, COUNT_CELL_HORIZONTAL**2)) for _ in range(50)]

    def build(self):
        for w in self.walls:
            w.draw()