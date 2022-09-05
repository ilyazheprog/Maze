from .config import *

import pygame

pygame.mixer.init()

collect = pygame.mixer.Sound('resources/sounds/collected.mp3')
crashing = pygame.mixer.Sound('resources/sounds/crashing into a wall.mp3')

collect.set_volume(global_settings["volume"]/100)
crashing.set_volume(global_settings["volume"]/100)