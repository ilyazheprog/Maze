from conf import *

from os import chdir, system

chdir(PATH)

match OS:
    case "Windows":
        with open(PATH+r"\run.bat", "w") as f:
            f.write(f"cd {PATH} && {PATH_TO_VENV}\\Scripts\\activate && "+r"python main.py && python .\src\check_reload.py")