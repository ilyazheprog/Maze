import pygame

from window import root
from config import *
from cell import Cell


class Floor:
    def __init__(self):
        self.floor = [[Cell((i, j), CELL_W, CELL_H) for i in range(0, W - CELL_W + 1, CELL_W)] for j in range(0, H - CELL_H + 1, CELL_H)]

    def draw(self):
        for row in self.floor:
            for c in row:
                c.draw()


fl = Floor()