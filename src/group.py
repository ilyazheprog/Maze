import pygame


class Group:
    def __init__(self):
        self.__group = []

    def add(self, *args):
        for e in args:
            self.__group.append(e)

    def draw(self, root):
        for e in self.__group:
            e.show(root)

    def manage_focus(self):
        for e in self.__group:
            e.manage_focus()

    def lock(self, item) -> None:
        for e in self.__group:
            if e.name == item:
                e.lock()
            else:
                e.unlock()

    def unlock_one(self, item) -> None:
        for e in self.__group:
            if e.name == item:
                e.unlock()
                return

    def __getitem__(self, item):
        for e in self.__group:
            if e.name == item:
                return e

