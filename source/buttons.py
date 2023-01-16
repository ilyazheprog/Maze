from game_engine.button import Button
from game_engine.group import Group
from config import *
from sounds import click

class MyBtn(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    @property
    def is_visible(self):
        return self._is_visible

    def vis(self):
        self._is_visible = True
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
        self._is_visible = False
    def manage_focus(self):
        x, y = pygame.mouse.get_pos()

        if self.is_locked:
            return self.lock()
        elif self.rect.collidepoint(x, y) and not self.is_focus:
            return self.focusing()
        elif not self.rect.collidepoint(x, y):
            return self.out_of_focusing()
        return self


pos_continue = W // 3 - W // 20, H - H // 5 - H // 10
pos_start = W // 4 + W // 25, H - H // 2 - H // 10
pos_settings = W // 4 + W // 50, H - H // 10 - 40
pos_menu = W // 3 + 40, H - H // 15 - 40

button_menu = MyBtn("To menu", "menu",  pos_menu, H // 15, sound_of_click_unlocked=click, bg_out_of_focus="violet")
button_continue = MyBtn("   Continue    ", "cont", pos_continue, font_size=H // 11, sound_of_click_unlocked=click, bg_out_of_focus="navy",)

pause_button_group = Group()
pause_button_group.add(button_menu, button_continue)

button_start = MyBtn("   Start    ", "start", pos_start, font_size=H // 8, sound_of_click_unlocked=click, bg_out_of_focus="navy")
button_settings = MyBtn("   Settings    ", "settings", pos_settings, font_size=H // 10, sound_of_click_unlocked=click, bg_out_of_focus="green")

menu_button_group = Group()
menu_button_group.add(button_start, button_settings)

pos_small = 10, H // 24 + H // 11 + H // 18 + 5
button_small = MyBtn("   Small   ", "sm", pos_small, font_size=H // 15, sound_of_click_unlocked=click, bg_out_of_focus="green")

pos_middle = 20 + button_small.x + button_small.width, button_small.y
button_middle = MyBtn("   Middle   ", "mid", pos_middle, font_size=H // 15, sound_of_click_unlocked=click, bg_out_of_focus="green")

pos_bigger = 20 + button_middle.x + button_middle.width, button_middle.y
button_bigger = MyBtn("   Bigger   ", "big", pos_bigger, font_size=H // 15, sound_of_click_unlocked=click, bg_out_of_focus="green")

window_mods = Group()
window_mods.add(button_small, button_middle, button_bigger)


pos_minus = 10, H // 4 + H // 11 + H // 18 - H // 25
button_minus = MyBtn("   -   ", "minus", pos_minus, font_size=H // 15, sound_of_click_unlocked=click, bg_out_of_focus="green")

pos_plus = 5 + 3 * button_minus.width, pos_minus[1]
button_plus = MyBtn("   +   ", "plus", pos_plus, font_size=H // 15, sound_of_click_unlocked=click, bg_out_of_focus="green")


pos_restart = pos_minus[0], H- H//5
button_restart = MyBtn("restart", "restart", pos_restart, font_size=H // 15, sound_of_click_unlocked=click, bg_out_of_focus="violet")

volume_button_group = Group()
volume_button_group.add(button_minus, button_plus)



pos_continue = W // 3 - W // 20, H - H // 5 - H // 10
pos_start = W // 4 + W // 25, H - H // 2 - H // 10
pos_settings = W // 4 + W // 50, H - H // 10 - 40
pos_menu = W // 3 + 40, H - H // 15 - 40

button_menu = MyBtn("To menu", "menu",  pos_menu, H // 15, sound_of_click_unlocked=click, bg_out_of_focus="violet")
button_continue = MyBtn("   Continue    ", "cont", pos_continue, font_size=H // 11, sound_of_click_unlocked=click, bg_out_of_focus="navy",)

pause_button_group = Group()
pause_button_group.add(button_menu, button_continue)

button_start = MyBtn("   Start    ", "start", pos_start, font_size=H // 8, sound_of_click_unlocked=click, bg_out_of_focus="navy")
button_settings = MyBtn("   Settings    ", "settings", pos_settings, font_size=H // 10, sound_of_click_unlocked=click, bg_out_of_focus="green")

menu_button_group = Group()
menu_button_group.add(button_start, button_settings)

pos_small = 10, H // 24 + H // 11 + H // 18 + 5
button_small = MyBtn("   Small   ", "sm", pos_small, font_size=H // 15, sound_of_click_unlocked=click, bg_out_of_focus="green")

pos_middle = 20 + button_small.x + button_small.width, button_small.y
button_middle = MyBtn("   Middle   ", "mid", pos_middle, font_size=H // 15, sound_of_click_unlocked=click, bg_out_of_focus="green")

pos_bigger = 20 + button_middle.x + button_middle.width, button_middle.y
button_bigger = MyBtn("   Bigger   ", "big", pos_bigger, font_size=H // 15, sound_of_click_unlocked=click, bg_out_of_focus="green")

window_mods = Group()
window_mods.add(button_small, button_middle, button_bigger)


pos_minus = 10, H // 4 + H // 11 + H // 18 - H // 25
button_minus = MyBtn("   -   ", "minus", pos_minus, font_size=H // 15, sound_of_click_unlocked=click, bg_out_of_focus="green")

pos_plus = 5 + 3 * button_minus.width, pos_minus[1]
button_plus = MyBtn("   +   ", "plus", pos_plus, font_size=H // 15, sound_of_click_unlocked=click, bg_out_of_focus="green")


pos_restart = pos_minus[0], H- H//5
button_restart = MyBtn("restart", "restart", pos_restart, font_size=H // 15, sound_of_click_unlocked=click, bg_out_of_focus="violet")

volume_button_group = Group()
volume_button_group.add(button_minus, button_plus)

