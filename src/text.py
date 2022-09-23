import pygame

from .config import *
from .button import *

pygame.font.init()

class Text:
    def __init__(self, text, font, size, pos, color=(255, 0, 0)):
        self.__text = text
        self.__font = font
        self.__size = size
        self.__color = color
        self.set_text(self.__text)
        self.__x, self.__y = pos
        self.__width, self.__height = self.__text2.get_size()

    def set_text(self, text):
        f2 = pygame.font.SysFont(self.__font, self.__size)
        self.__text2 = f2.render(text, False, self.__color)
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def pos(self):
        return self.__x, self.__y

    @pos.setter
    def pos(self, value):
        self.__x, self.__y = value
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def draw(self, surface):
        surface.blit(self.__text2, (self.__x, self.__y))


settings_ = Text("Settings", "Arial", H // 12, (W // 4 + W // 9, H // 24))
size = Text("Size of window: ", "Arial", H // 18, (10, H // 24 + H // 11), color=pygame.Color("orange"))
volume = Text("Volume: ", "Arial", H // 18, (10, 10 + button_small.y + button_small.height), color=pygame.Color("orange"))
skin = Text("Skin: ", "Arial", H // 18, (10, button_test.y + button_test.height +10), color=pygame.Color("orange"))
volume_numm = Text(str(global_settings["volume"]), "Arial", H // 18, [0, 0], color=pygame.Color("violet"))
cur_score_in_game = Text("", "Arial", 40, (W // 2 - 50, H // 2 - 50))
cur_score_in_pause = Text("", "Arial", H // 9, (W // 5, H // 3 + 80), GREEN)
paused = Text("Paused", "Arial", H // 5, (W // 4, H // 10))
