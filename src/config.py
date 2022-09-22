import pygame

from os.path import exists
from json import loads, dumps

# Colors
WHITE = 255, 255, 255
BLUE = 0, 70, 225
YELLOW = 230, 255, 80
GREEN = 0, 255, 0
EXP = 122, 43, 237
ORANGE = 219, 124, 0
COLOR_CHOSEN_AND_BLOCKED = "gray"

# Player
COLOR_FOR_PLAYER = ORANGE
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

if not exists("src/config.json"):
    global_settings = {"window": 2, "volume": 50}
    with open("src/config.json", "w") as f:
        f.write(dumps(global_settings, indent=4))
    COUNT_CELL_HORIZONTAL = COUNT_CELL_VERTICAL = MIDDLE
else:
    with open("src/config.json") as f:
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
