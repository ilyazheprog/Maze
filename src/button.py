from .config_color import *
from .sounds import click
from .config import *
from .group import Group

import pygame
from pygame.mixer import Sound

pygame.font.init()

font = pygame.font.SysFont("Arial", 20)


class Button:
    def __init__(self, text: str, name: str, pos: tuple[int, int], font_size: int, bg_out_of_focus: str = "black",
                 bg_focus: str = "orange", sound_of_click_unlocked: None | Sound = click, is_focus: bool = False, is_locked: bool = False, is_visible: bool = True):
        self.__sound_of_click_unlocked = sound_of_click_unlocked
        self.__type = "btn"
        self.__is_visible = is_visible
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
        return self.__type

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

    @property
    def is_visible(self):
        return self.__is_visible

    def vis(self):
        self.__is_visible = True
    def focusing(self):
        self.change_text(self.bg_focus)
        self.is_focus = True

    def out_of_focusing(self):
        self.change_text(self.bg_out_of_focus)
        self.is_focus = False

    def lock(self):
        self.is_locked = True
        self.change_text(COLOR_CHOSEN_AND_BLOCKED)

    def unlock(self):
        self.is_locked = False
        self.change_text(self.bg_out_of_focus)

    def invis(self):
        self.__is_visible = False
    def manage_focus(self):
        x, y = pygame.mouse.get_pos()

        if self.is_locked:
            return self.lock()
        elif self.rect.collidepoint(x, y) and not self.is_focus:
            return self.focusing()
        elif not self.rect.collidepoint(x, y):
            return self.out_of_focusing()
        return self

    def change_text(self, bg="black"):
        """Change the text whe you click"""
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.__x, self.__y, self.size[0], self.size[1])

    def show(self, root):
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
pos_continue = W // 3 - W // 20, H - H // 5 - H // 10
pos_start = W // 4 + W // 25, H - H // 2 - H // 10
pos_settings = W // 4 + W // 50, H - H // 10 - 40
pos_menu = W // 3 + 40, H - H // 15 - 40

button_menu = Button("To menu", "menu",  pos_menu, H // 15, bg_out_of_focus="violet")
button_continue = Button("   Continue    ", "cont", pos_continue, font_size=H // 11, bg_out_of_focus="navy",)

pause_button_group = Group()
pause_button_group.add(button_menu, button_continue)

button_start = Button("   Start    ", "start", pos_start, font_size=H // 8, bg_out_of_focus="navy")
button_settings = Button("   Settings    ", "settings", pos_settings, font_size=H // 10, bg_out_of_focus="green")

menu_button_group = Group()
menu_button_group.add(button_start, button_settings)

pos_small = 10, H // 24 + H // 11 + H // 18 + 5
button_small = Button("   Small   ", "sm", pos_small, font_size=H // 15, bg_out_of_focus="green")

pos_middle = 20 + button_small.x + button_small.width, button_small.y
button_middle = Button("   Middle   ", "mid", pos_middle, font_size=H // 15, bg_out_of_focus="green")

pos_bigger = 20 + button_middle.x + button_middle.width, button_middle.y
button_bigger = Button("   Bigger   ", "big", pos_bigger, font_size=H // 15, bg_out_of_focus="green")

window_mods = Group()
window_mods.add(button_small, button_middle, button_bigger)


pos_minus = 10, H // 4 + H // 11 + H // 18 - H // 25
button_minus = Button("   -   ", "minus", pos_minus, font_size=H // 15, bg_out_of_focus="green")

pos_plus = 5 + 3 * button_minus.width, pos_minus[1]
button_plus = Button("   +   ", "plus", pos_plus, font_size=H // 15, bg_out_of_focus="green")


volume_button_group = Group()
volume_button_group.add(button_minus, button_plus)

