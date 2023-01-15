import pygame


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
