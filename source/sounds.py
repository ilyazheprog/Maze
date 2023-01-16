from config import global_settings
from game_engine.sound import Sound

collect = Sound('resources/sounds/collected.mp3')
crashing = Sound('resources/sounds/crashing into a wall.mp3')
click = Sound('resources/sounds/click.mp3')

collect.set_volume(global_settings["volume"]/100)
crashing.set_volume(global_settings["volume"]/100)
click.set_volume(global_settings["volume"]/100)