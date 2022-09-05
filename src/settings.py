import pygame
from pygame.locals import *

from .config import *
from .text import Text
from .button import *


class Settings:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.bg = BACKGROUND_IMAGE_OBJ

        self.pos_small = 10, H // 24 + H // 11 + H // 18

        self.button_small = ButtonSetSize("   Small    ", self.pos_small, font=H // 15, bg="green")
        self.pos_middle = 20 + self.button_small.size[0], H // 24 + H // 11 + H // 18
        self.button_middle = ButtonSetSize("   Middle    ", self.pos_middle, font=H // 15, bg="green")

        self.pos_bigger = 30 + self.button_small.size[0] + self.button_middle.size[0], H // 24 + H // 11 + H // 18
        self.button_bigger = ButtonSetSize("   Bigger    ", self.pos_bigger, font=H // 15, bg="green")

        self.pos_minus = 10, H // 4 + H // 11 + H//18
        self.button_minus = ButtonSetVolume("   -   ", self.pos_minus, font=H // 15, bg="green")

        self.pos_plus = 100+self.button_minus.size[0], H // 4 + H // 11 + H // 18
        self.button_plus = ButtonSetVolume("   +   ", self.pos_plus, font=H // 15, bg="green")

    def run(self, root):
        root.set_capture("Maze [settings]")
        root.fill(img=self.bg)

        if CHOSEN == "SMALL":
            self.button_small = self.button_small.lock()
        elif CHOSEN == "MIDDLE":
            self.button_middle = self.button_middle.lock()
        else:
            self.button_bigger = self.button_bigger.lock()

        if global_settings["volume"] == 100:
            self.button_plus = self.button_plus.lock()
        elif global_settings["volume"] == 0:
            self.button_minus = self.button_minus.lock()

        while True:
            root.fill(img=self.bg)
            _settings = Text("Settings", "Arial", H // 12)
            _settings.draw(root.screen, W // 4 + W // 9, H // 24)

            size = Text("Size of window: ", "Arial", H // 18, color=pygame.Color("orange"))
            size.draw(root.screen, 10, H // 24 + H // 11)

            volume = Text("Volume: ", "Arial", H // 18, color=pygame.Color("orange"))
            volume.draw(root.screen, 10, H // 4 + H // 11)

            _volume = Text(str(global_settings["volume"]), "Arial", H // 18, color=pygame.Color("violet"))
            _volume.draw(root.screen, 25 + self.button_minus.size[0], self.pos_minus[1] + 5)

            Text("Changes will take effect after restarting the game*", "Consolas", H // 29,
                 color=pygame.Color("black")) \
            .draw(root.screen, 15, H - H // 19)
            self.button_small.show(root)
            self.button_middle.show(root)
            self.button_bigger.show(root)

            self.button_minus.show(root)
            self.button_plus.show(root)


            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                    root.exit()

                self.button_small=self.button_small.have_focus()
                self.button_middle=self.button_middle.have_focus()
                self.button_bigger=self.button_bigger.have_focus()

                self.button_minus=self.button_minus.have_focus()
                self.button_plus=self.button_plus.have_focus()


                if self.button_small.click(event, root):
                    self.button_small=self.button_small.lock()
                    self.button_middle=self.button_middle.unlock()
                    self.button_bigger=self.button_bigger.unlock()
                    global_settings["window"] = 0

                elif self.button_middle.click(event, root):
                    self.button_small = self.button_small.unlock()
                    self.button_middle = self.button_middle.lock()
                    self.button_bigger = self.button_bigger.unlock()
                    global_settings["window"] = 1

                elif self.button_bigger.click(event, root):
                    self.button_small = self.button_small.unlock()
                    self.button_middle = self.button_middle.unlock()
                    self.button_bigger = self.button_bigger.lock()
                    global_settings["window"] = 2

                elif (self.button_minus.click(event, root) or pygame.key.get_pressed()[K_DOWN]) and not self.button_minus.is_locked:
                    global_settings["volume"] -= 1
                    if self.button_plus.is_locked:
                        self.button_plus=self.button_plus.unlock()
                    _volume = Text(str(global_settings["volume"]), "Arial", H // 18, color=pygame.Color("violet"))
                    _volume.draw(root.screen, 25 + self.button_minus.size[0], self.pos_minus[1] + 5)
                    if global_settings["volume"] == 0:
                        self.button_minus = self.button_minus.lock()

                elif (self.button_plus.click(event, root)  or pygame.key.get_pressed()[K_UP]) and not self.button_plus.is_locked:
                    global_settings["volume"] += 1
                    if self.button_minus.is_locked:
                        self.button_minus = self.button_minus.unlock()
                    _volume = Text(str(global_settings["volume"]), "Arial", H // 18, color=pygame.Color("violet"))
                    _volume.draw(root.screen, 25 + self.button_minus.size[0], self.pos_minus[1] + 5)
                    if global_settings["volume"] == 100:
                        self.button_plus = self.button_plus.lock()

            pygame.display.update()
            self.clock.tick(24)


settings = Settings()
