import pygame
from pygame.mixer import Sound

pygame.font.init()

font = pygame.font.SysFont("Arial", 20)


class Button:
    def __init__(self, text: str, name: str, pos: tuple[int, int], font_size: int, bg_out_of_focus: str = "black",
                 bg_focus: str = "orange", sound_of_click_unlocked: None | Sound = None, is_focus: bool = False, is_locked: bool = False, is_visible: bool = True):
        self.__sound_of_click_unlocked = sound_of_click_unlocked
        self._type = "btn"
        self._is_visible = is_visible
        self.name = name
        self.is_focus = is_focus
        self.bg_out_of_focus = bg_out_of_focus
        self.bg_focus = bg_focus
        self.__x, self.__y = pos
        self.text = text
        self.font = pygame.font.SysFont("Arial", font_size)

        self.text = self.font.render(text, True, pygame.Color("White"))

        self.size = self.text.get_size()
        self.bg = bg_out_of_focus
        self.is_locked = is_locked
        self.change_text(bg_out_of_focus)

    @property
    def type(self):
        return self._type

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    def change_text(self, bg="black"):
        """Change the text whe you click"""
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.__x, self.__y, self.size[0], self.size[1])

    def draw(self, root):
        root.screen.blit(self.surface, (self.__x, self.__y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    if self.__sound_of_click_unlocked is not None:
                        self.__sound_of_click_unlocked.play()
                    return True



# Buttons
