import numpy as np
import colorama
from colorama import Fore , Back , Style
from buildings import *
from movingObjects import *
from others import *
from spells import *
from map import *

colorama.init(autoreset=True)
gameStatus ="playing"

if __name__ == "__main__":
    map1 = map(30, 90, 0, 0)
    map1.createMap()
    map1.drawMap()
    texture, h, w = getTexture("../textures/king.txt")
    print(texture)

