import pygame

import sys

class Window:
    def __init__(self, size, capture):
        self._score_visible = False
        self._display = pygame.display
        self._screen = self._display.set_mode(size)
        self._capture = capture
        self._score = None
        self._minimized = False

    @property
    def screen(self):
        return self._screen

    def update(self):
        self._display.update()

    def fill(self, color=None, img=None):
        if color is not None:
            self.screen.fill(color)
        else:
            self.screen.blit(img, (0, 0))

    def set_capture(self, capture):
        self._display.set_caption(capture)

    @staticmethod
    def exit():
        pygame.quit()
        sys.exit()

    def listen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()

