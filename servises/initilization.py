from conf import *

from os import chdir, system

chdir(PATH)

match OS:
    case "Windows":
       system(f"cd {PATH}\\source && git clone https://github.com/Ilya484/game_engine.git && cd ..")
       with open(PATH+r"\run.bat", "w") as f:
            f.write(f"{PATH_TO_VENV}\\Scripts\\activate && "+r"python .\source\main.py && python .\servises\check_reload.py")