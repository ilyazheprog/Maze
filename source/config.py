from config_color import *
import pygame

from os.path import exists
from json import loads, dumps


def rewrite(gs):
    with open("data/config.json", "w") as f:
        f.write(dumps(gs, indent=4))


# Player
R = 17


# Sizes
SMALL = 10
MIDDLE = 17
BIGGER = 23

# Cell
BORDER = 1
CELL_W = 2 * R
CELL_H = 2 * R


COUNT_CELL_HORIZONTAL = COUNT_CELL_VERTICAL = None

if not exists("data/config.json"):
    global_settings = {"window": 2, "volume": 50, "skin": GREEN, "reload": False}
    rewrite(global_settings)
    COUNT_CELL_HORIZONTAL = COUNT_CELL_VERTICAL = MIDDLE
else:
    with open("data/config.json") as f:
        global_settings = loads(f.read())
        match int(global_settings["window"]):
            case 0:
                COUNT_CELL_HORIZONTAL = COUNT_CELL_VERTICAL = SMALL
            case 1:
                COUNT_CELL_HORIZONTAL = COUNT_CELL_VERTICAL = MIDDLE
            case 2:
                COUNT_CELL_HORIZONTAL = COUNT_CELL_VERTICAL = BIGGER

# Window
W = H = CELL_W*COUNT_CELL_HORIZONTAL+BORDER

# Other
FPS = 20
BACKGROUND_IMAGE_PATH = "resources/images/pause background.png"
BACKGROUND_IMAGE_OBJ = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE_PATH), (W, H))
