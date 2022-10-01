import pygame
from pygame.locals import *

from .text import *
from .button import window_mods, volume_button_group
from .sounds import collect
from .skins import skins


class Settings:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.bg = BACKGROUND_IMAGE_OBJ

    def run(self, root):
        root.set_capture("Maze [settings]")
        root.fill(img=self.bg)

        if global_settings["window"] == 0:
            window_mods.lock("sm")
        elif global_settings["window"] == 1:
            window_mods.lock("mid")
        else:
            window_mods.lock("big")

        if global_settings["volume"] == 100:
            volume_button_group.lock("plus")
        elif global_settings["volume"] == 0:
            volume_button_group.lock("minus")

        while True:
            root.fill(img=self.bg)

            settings_.show(root.screen)
            size.show(root.screen)
            volume.show(root.screen)

            __pos_volume = [W//9 + button_minus.size[0], pos_minus[1] + 5]
            if global_settings["volume"] == 100:
                __pos_volume[0] = W//12 + button_minus.size[0]
            elif 10 <= global_settings["volume"]<=99:
                __pos_volume[0] = W//10 + button_minus.size[0]

            volume_numm.pos = __pos_volume
            volume_numm.show(root.screen)
                
            Text("Changes will take effect after restarting the game*", "Consolas", H // 29, (15, H - H // 19),
                 color=pygame.Color("black")).show(root.screen)

            # Draw buttons
            window_mods.draw(root)
            volume_button_group.draw(root)
            skins.draw(root)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                    root.exit()

                # Change button color on hover
                window_mods.manage_focus()
                volume_button_group.manage_focus()

                # Re-show buttons
                window_mods.draw(root)
                volume_button_group.draw(root)

                skins.draw(root)
                # Handling clicks
                if skins["yellow"].click(event):
                    skins.lock("yellow")
                elif skins["green"].click(event):
                    skins.lock("green")
                elif window_mods["sm"].click(event):
                    window_mods.lock("sm")
                    global_settings["window"] = 0
                elif window_mods["mid"].click(event):
                    window_mods.lock("mid")
                    global_settings["window"] = 1
                elif window_mods["big"].click(event):
                    window_mods.lock("big")
                    global_settings["window"] = 2

                elif (volume_button_group["minus"].click(event) or pygame.key.get_pressed()[K_DOWN]) and not button_minus.is_locked:
                    global_settings["volume"] -= 1
                    if button_plus.is_locked:
                        volume_button_group.unlock_one("plus")

                elif (button_plus.click(event) or pygame.key.get_pressed()[K_UP]) and not button_plus.is_locked:
                    global_settings["volume"] += 1
                    if button_minus.is_locked:
                        volume_button_group.unlock_one("minus")

                elif button_test.click(event):
                    collect.set_volume(global_settings["volume"]/100)
                    collect.play()

                __pos_volume = [W // 9 + button_minus.size[0], pos_minus[1] + 5]
                if global_settings["volume"] == 100:
                    __pos_volume[0] = W // 12 + button_minus.size[0]
                elif 10 <= global_settings["volume"] <= 99:
                    __pos_volume[0] = W // 10 + button_minus.size[0]

                volume_numm.set_text(str(global_settings["volume"]))
                volume_numm.pos = __pos_volume
                volume_numm.show(root.screen)

                if global_settings["volume"] == 0:
                    button_minus.lock()
                elif global_settings["volume"] == 100:
                    button_plus.lock()
            pygame.display.update()
            self.clock.tick(24)


settings = Settings()
