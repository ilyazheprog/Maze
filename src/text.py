import pygame


class Text:
    def __init__(self, text, font, size):
        f2 = pygame.font.SysFont(font, size)
        self.text2 = f2.render(text, False,
                          (255, 0, 0))

    def draw(self, surface, *pos):
        surface.blit(self.text2, pos)

