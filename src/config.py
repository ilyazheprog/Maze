import pygame


from os import getcwd
from os.path import exists, abspath
from json import loads, dumps

PATH = abspath("cell.py")
PATH = PATH[:PATH.rfind("\\")]
# Colors
WHITE = 255, 255, 255
BLUE = 0, 70, 225
YELLOW = 230, 255, 80
GREEN = 0, 255, 0
EXP = 122, 43, 237
COLOR_CHOsZEN = "gray"

# Player
COLOR_FOR_PLAYER = BLUE
R = 17

# Sizes
SMALL = 10
MIDDLE = 17
BIGGER = 23
CHOSEN = None

# Cell
BORDER = 1
CELL_W = 2 * R
CELL_H = 2 * R

VOLUME = None

COUNT_CELL_HORIZONTAL = COUNT_CELL_VERTICAL = None
if not exists("src/config.json"):
    global_settings = {"window": 2, "volume": 50}
    with open("src/config.json", "w") as f:
        f.write(dumps(global_settings, indent=4))
    COUNT_CELL_HORIZONTAL = COUNT_CELL_VERTICAL = MIDDLE
    CHOSEN = "MIDDLE"
    VOLUME = 1
else:
    with open("src/config.json") as f:
        global_settings = loads(f.read())
        match int(global_settings["window"]):
            case 0:
                COUNT_CELL_HORIZONTAL = COUNT_CELL_VERTICAL = SMALL
                CHOSEN = "SMALL"
            case 1:
                COUNT_CELL_HORIZONTAL = COUNT_CELL_VERTICAL = MIDDLE
                CHOSEN = "MIDDLE"
            case 2:
                COUNT_CELL_HORIZONTAL = COUNT_CELL_VERTICAL = BIGGER
                CHOSEN = "BIGGER"
        VOLUME = global_settings["volume"]

# Window
W = H = CELL_W*COUNT_CELL_HORIZONTAL+BORDER


# Other
FPS = 20
BACKGROUND_IMAGE_PATH = "resources/images/pause background.png"
BACKGROUND_IMAGE_OBJ = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE_PATH), (W, H))
