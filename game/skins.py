import pygame

from .config_color import *
from src.group import Group


class Skin:
    def __init__(self, pos: tuple[int, int], name: str, color: str = "black", border_color: str = "red",
                 is_chosen: bool = False):
        self.__type = "skin"
        self.name = name
        self.__border_color = border_color
        self.__x, self.__y = pos
        self.__is_chosen = is_chosen
        self.__color = color
        self.__R = 50
        self.__collider = pygame.Rect(self.__x, self.__y, 2 * self.__R, 2 * self.__R)

    @property
    def type(self):
        return self.__type

    def draw(self, root):
        pygame.draw.circle(root.screen, self.__color, (self.__x + self.__R, self.__y + self.__R), self.__R)
        if self.__is_chosen:
            pygame.draw.circle(root.screen, self.__border_color, (self.__x + self.__R, self.__y + self.__R), self.__R, width=5)

    def click(self, event):
        x, y = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.__collider.collidepoint(x, y):
                    return not self.__is_chosen

    def lock(self):
        self.__is_chosen = True

    def unlock(self):
        self.__is_chosen = False


skin_yellow = Skin((300, 400), "yellow", color=YELLOW)
skin_green = Skin((200, 400), "green", color=GREEN)

skins = Group()
skins.add(skin_yellow, skin_green)