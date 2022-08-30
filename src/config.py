import pygame


from os import getcwd
from os.path import exists, abspath

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


COUNT_CELL_HORIZONTAL = COUNT_CELL_VERTICAL = None
if not exists("src/size window"):
    with open("src/size window", "w") as f:
        f.write("MIDDLE")
    COUNT_CELL_HORIZONTAL = COUNT_CELL_VERTICAL = MIDDLE
    CHOSEN = "MIDDLE"
else:
    with open("src/size window") as f:
        match f.readline():
            case "SMALL":
                COUNT_CELL_HORIZONTAL = COUNT_CELL_VERTICAL = SMALL
                CHOSEN = "SMALL"
            case "MIDDLE":
                COUNT_CELL_HORIZONTAL = COUNT_CELL_VERTICAL = MIDDLE
                CHOSEN = "MIDDLE"
            case "BIGGER":
                COUNT_CELL_HORIZONTAL = COUNT_CELL_VERTICAL = BIGGER
                CHOSEN = "BIGGER"


# Window
W = H = CELL_W*COUNT_CELL_HORIZONTAL+BORDER


# Other
FPS = 20
BACKGROUND_IMAGE_PATH = "resources/images/pause background.png"
BACKGROUND_IMAGE_OBJ = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE_PATH), (W, H))
