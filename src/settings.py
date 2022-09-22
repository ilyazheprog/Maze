import pygame
from pygame.locals import *
from .text import Text
from .button import *
from .sounds import collect


class Settings:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.bg = BACKGROUND_IMAGE_OBJ

    def run(self, root):
        root.set_capture("Maze [settings]")
        root.fill(img=self.bg)

        if global_settings["window"] == 0:
            button_small.lock()
        elif global_settings["window"] == 1:
            button_middle.lock()
        else:
            button_bigger.lock()

        if global_settings["volume"] == 100:
            button_plus.lock()
        elif global_settings["volume"] == 0:
            button_minus.lock()

        while True:
            root.fill(img=self.bg)
            _settings = Text("Settings", "Arial", H // 12)
            _settings.draw(root.screen, W // 4 + W // 9, H // 24)

            size = Text("Size of window: ", "Arial", H // 18, color=pygame.Color("orange"))
            size.draw(root.screen, 10, H // 24 + H // 11)

            volume = Text("Volume: ", "Arial", H // 18, color=pygame.Color("orange"))
            volume.draw(root.screen, 10, H // 4 + H // 11)

            _volume = Text(str(global_settings["volume"]), "Arial", H // 18, color=pygame.Color("violet"))
            __pos_volume = [W//9 + button_minus.size[0], pos_minus[1] + 5]
            if global_settings["volume"] == 100:
                __pos_volume[0] = W//12 + button_minus.size[0]
            elif 10 <= global_settings["volume"]<=99:
                __pos_volume[0] = W//10 + button_minus.size[0]
            _volume.draw(root.screen, *__pos_volume)
                
            Text("Changes will take effect after restarting the game*", "Consolas", H // 29,
                 color=pygame.Color("black")).draw(root.screen, 15, H - H // 19)

            # Draw buttons
            button_small.show(root)
            button_middle.show(root)
            button_bigger.show(root)

            button_minus.show(root)
            button_plus.show(root)

            button_test.show(root)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                    root.exit()

                # Change button color on hover
                button_small.manage_focus()
                button_middle.manage_focus()
                button_bigger.manage_focus()
                button_minus.manage_focus()
                button_plus.manage_focus()
                button_test.manage_focus()

                # Re-draw buttons
                button_small.show(root)
                button_middle.show(root)
                button_bigger.show(root)
                button_minus.show(root)
                button_plus.show(root)
                button_test.show(root)

                # Handling clicks
                if button_small.click(event):
                    button_small.lock()
                    button_middle.unlock()
                    button_bigger.unlock()
                    global_settings["window"] = 0
                elif button_middle.click(event):
                    button_small.unlock()
                    button_middle.lock()
                    button_bigger.unlock()
                    global_settings["window"] = 1
                elif button_bigger.click(event):
                    button_small.unlock()
                    button_middle.unlock()
                    button_bigger.lock()
                    global_settings["window"] = 2

                elif (button_minus.click(event) or pygame.key.get_pressed()[K_DOWN]) and not button_minus.is_locked:
                    global_settings["volume"] -= 1
                    if button_plus.is_locked:
                        button_plus.unlock()

                elif (button_plus.click(event) or pygame.key.get_pressed()[K_UP]) and not button_plus.is_locked:
                    global_settings["volume"] += 1
                    if button_minus.is_locked:
                        button_minus.unlock()

                elif button_test.click(event):
                    collect.set_volume(global_settings["volume"]/100)
                    collect.play()

                __pos_volume = [W // 9 + button_minus.size[0], pos_minus[1] + 5]
                if global_settings["volume"] == 100:
                    __pos_volume[0] = W // 12 + button_minus.size[0]
                elif 10 <= global_settings["volume"] <= 99:
                    __pos_volume[0] = W // 10 + button_minus.size[0]
                _volume.draw(root.screen, *__pos_volume)

                if global_settings["volume"] == 0:
                    button_minus.lock()
                elif global_settings["volume"] == 100:
                    button_plus.lock()
            pygame.display.update()
            self.clock.tick(24)


settings = Settings()
