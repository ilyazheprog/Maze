import pygame

from random import randint, seed as se
from .config import *
from .wall import Wall
from .exp import *
from .floor import fl


class Maze:
    def __init__(self, seed=None):
        self.__walls = self.generate_walls(seed)
        self.__exps = self.generate_exps(seed)

    @property
    def exps(self):
        return self.__exps

    def remove(self, cell):
        fl[cell].is_exp = False
        self.__exps[cell] = None

    def generate_walls(self, seed=None):
        if seed is not None:
            se(seed)
        _walls = [None for _ in range(COUNT_CELL_HORIZONTAL**2)]
        for _ in range(50):
            cell = randint(1, COUNT_CELL_HORIZONTAL ** 2 -1)
            fl[cell].is_wall = True
            _walls[cell] = Wall(cell)

        return _walls

    def generate_exps(self, seed=None):
        if seed is not None:
            se(seed)
        _exps = [None for _ in range(COUNT_CELL_HORIZONTAL**2)]

        for _ in range(10):
            cell = randint(1, COUNT_CELL_VERTICAL ** 2 - 1)

            while fl[cell].is_wall or fl[cell].is_exp:
                cell = randint(1, COUNT_CELL_VERTICAL ** 2 - 1)

            fl[cell].is_exp = True
            _exps[cell] = Exp(cell)

        return _exps

    def build(self, surface):
        fl.draw(surface)

        for w in self.__walls:
            if w is not None:
                w.draw(surface)

        for e in self.__exps:
            if e is not None:
                e.draw(surface)


maze = Maze()
