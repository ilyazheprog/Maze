# Maze

## How to install
We clone the code from the repository with the command: `git clone https://github.com/Ilya484/Maze.git`.

## Initialization
In the `conf.py` file, in the `OS` variable, write the name of your operating system, in `PATH` - the absolute path to the project, in `PATH_TO_VENV` - the absolute path to the virtual environment.

For example,

```python
OS = "Windows"
PATH = r"C:\Maze"
PATH_TO_VENV = r"C:\venv"
```

Run `initilization.py`.

Note: for now, initialization is automated only for Windows!

**You must install all dependencies from `req.txt` into the virtual environment yourself!**

## launch
After initialization, `run.bat` or `run.sh` will appear, depending on the operating system. To open the game you need to run this file.

## Controls
`←, ↑, →, ↓` - to move the player

`S` - to draw/hide the score

`Q` - to close the game window

`ESC` - to enter/exit pause mode