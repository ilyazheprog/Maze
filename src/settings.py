import pygame
from pygame.locals import *
import decouple

from .config import rewrite
from .player import player
from .text import *
from .sounds import collect
from .button import window_mods, volume_button_group, button_restart

from .skins import skins


class Settings:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.bg = BACKGROUND_IMAGE_OBJ

    def run(self, root):
        root.set_capture("Maze [settings]")
        root.fill(img=self.bg)

        self.__init_screen()

        while True:
            root.fill(img=self.bg)

            settings_.draw(root.screen)
            size.draw(root.screen)
            volume.draw(root.screen)

            __pos_volume = [W // 9 + button_minus.size[0], pos_minus[1] + 5]
            if global_settings["volume"] == 100:
                __pos_volume[0] = W // 12 + button_minus.size[0]
            elif 10 <= global_settings["volume"] <= 99:
                __pos_volume[0] = W // 10 + button_minus.size[0]

            volume_numm.pos = __pos_volume
            volume_numm.draw(root.screen)

            Text("Changes will take effect after restarting the game*", "Consolas", H // 29, (15, H - H // 19),
                 color=pygame.Color("black")).draw(root.screen)

            # Draw buttons
            window_mods.draw(root)
            volume_button_group.draw(root)
            skins.draw(root)
            button_restart.draw(root)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                    root.exit()

                # Change button color on hover
                window_mods.manage_focus()
                volume_button_group.manage_focus()
                button_restart.manage_focus()

                # Re-draw buttons
                window_mods.draw(root)
                volume_button_group.draw(root)
                button_restart.draw(root)
                skins.draw(root)
                button_restart.draw(root)

                # Handling clicks
                self.__manage_button_click(root, event)

                __pos_volume = [W // 9 + button_minus.size[0], pos_minus[1] + 5]
                if global_settings["volume"] == 100:
                    __pos_volume[0] = W // 12 + button_minus.size[0]
                elif 10 <= global_settings["volume"] <= 99:
                    __pos_volume[0] = W // 10 + button_minus.size[0]

                volume_numm.set_text(str(global_settings["volume"]))
                volume_numm.pos = __pos_volume
                volume_numm.draw(root.screen)

            pygame.display.update()
            self.clock.tick(24)

    @staticmethod
    def __manage_button_click(root, event):
        if button_restart.click(event):
            global_settings["reload"] = True
            root.exit()

        elif skins["yellow"].click(event):
            skins.lock("yellow")
            player.edit_color(YELLOW)
            global_settings["skin"] = YELLOW

        elif skins["green"].click(event):
            skins.lock("green")
            player.edit_color(GREEN)
            global_settings["skin"] = GREEN

        elif window_mods["sm"].click(event):
            window_mods.lock("sm")
            global_settings["window"] = 0
        elif window_mods["mid"].click(event):
            window_mods.lock("mid")
            global_settings["window"] = 1
        elif window_mods["big"].click(event):
            window_mods.lock("big")
            global_settings["window"] = 2

        elif (volume_button_group["minus"].click(event) or pygame.key.get_pressed()[K_DOWN]) and \
                volume_button_group["minus"].is_visible:
            global_settings["volume"] -= 1
            click.set_volume(global_settings["volume"] / 100)
            if global_settings["volume"] == 0:
                volume_button_group.invis("minus")
            elif global_settings["volume"] == 99:
                volume_button_group.vis("plus")

        elif (volume_button_group["plus"].click(event) or pygame.key.get_pressed()[K_UP]) and \
                volume_button_group["plus"].is_visible:
            global_settings["volume"] += 1
            click.set_volume(global_settings["volume"] / 100)
            if global_settings["volume"] == 100:
                volume_button_group.invis("plus")
            elif global_settings["volume"] == 1:
                volume_button_group.vis("minus")

    @staticmethod
    def __init_screen():
        if global_settings["window"] == 0:
            window_mods.lock("sm")
        elif global_settings["window"] == 1:
            window_mods.lock("mid")
        else:
            window_mods.lock("big")

        if global_settings["volume"] == 100:
            volume_button_group.invis("plus")
        elif global_settings["volume"] == 0:
            volume_button_group.invis("minus")

        if all(a == b for a, b in zip(global_settings["skin"], GREEN)):
            skins.lock("green")
            player.edit_color(GREEN)
        elif all(a == b for a, b in zip(global_settings["skin"], YELLOW)):
            skins.lock("yellow")
            player.edit_color(YELLOW)


settings = Settings()
