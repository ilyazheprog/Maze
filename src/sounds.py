from .config import global_settings
import pygame

pygame.mixer.init()

class Sound:
    def __init__(self, path: str):
        self.__pg_sound = pygame.mixer.Sound(path)

    def set_volume(self, value: int | float):
        self.__pg_sound.set_volume(value)

    def play(self):
        self.__pg_sound.play()

# Sound
collect = Sound('resources/sounds/collected.mp3')
crashing = Sound('resources/sounds/crashing into a wall.mp3')
click = Sound('resources/sounds/click.mp3')

collect.set_volume(global_settings["volume"]/100)
crashing.set_volume(global_settings["volume"]/100)
click.set_volume(global_settings["volume"]/100)
