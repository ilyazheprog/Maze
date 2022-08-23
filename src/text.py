import pygame


class Text:
    def __init__(self, text, font, size, color=(255, 0, 0)):
        f2 = pygame.font.SysFont(font, size)
        self.text2 = f2.render(text, False, color)

    def draw(self, surface, *pos):
        surface.blit(self.text2, pos)

