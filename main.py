import numpy as np
import colorama
from colorama import Fore , Back , Style
from buildings import *
from movingObjects import *
from spawningPoints import *
from spells import *
from map import *

colorama.init(autoreset=True)
gameStatus ="playing"

if __name__ == "__main__":
    map1 = map(20, 20, 0, 0)
    map1.make_canvas()
    map1.draw_canvas()

