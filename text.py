import pygame
from window import root

class Text:
    def __init__(self, text, font, size):
        f2 = pygame.font.SysFont(font, size)
        self.text2 = f2.render(text, False,
                          (0, 180, 0))

    def draw(self, pos):
        root.screen.blit(self.text2, pos)