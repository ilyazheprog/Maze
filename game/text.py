from src.text import Text
from .config import *
from .buttons import *


settings_ = Text("Settings", "Arial", H // 12, (W // 4 + W // 9, H // 24))
size = Text("Size of window: ", "Arial", H // 18, (10, H // 24 + H // 11), color=pygame.Color("orange"))
volume = Text("Volume: ", "Arial", H // 18, (10, 10 + button_small.y + button_small.height), color=pygame.Color("orange"))
skin = Text("Skin: ", "Arial", H // 18, (10, button_minus.y + button_minus.height +10), color=pygame.Color("orange"))
volume_numm = Text(str(global_settings["volume"]), "Arial", H // 18, [0, 0], color=pygame.Color("violet"))
cur_score_in_game = Text("", "Arial", 40, (W // 2 - 50, H // 2 - 50))
cur_score_in_pause = Text("", "Arial", H // 9, (W // 5, H // 3 + 80), GREEN)
paused = Text("Paused", "Arial", H // 5, (W // 4, H // 10))
