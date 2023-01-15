import pygame

pygame.mixer.init()

class Sound:
    def __init__(self, path: str):
        self.__pg_sound = pygame.mixer.Sound(path)

    def set_volume(self, value: int | float):
        self.__pg_sound.set_volume(value)

    def play(self):
        self.__pg_sound.play()
