import pygame

from random import randint

from .config import *
from .wall import Wall


class Maze:
    def __init__(self):
        self.walls = [Wall((randint(0, W), randint(0, H)), 20, randint(10, 80)) for _ in range(10)]

    def build(self):
        for w in self.walls:
            w.draw()