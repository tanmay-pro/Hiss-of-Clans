import numpy as np
import colorama
import os
from colorama import Fore, Back, Style
from buildings import *
from movingObjects import *
from others import *
from spells import *
from map import *
from input import *

colorama.init(autoreset=True)
gameStatus = "playing"

if __name__ == "__main__":
    mainMap = map(30, 90, 0, 0, 2, 1)
    mainMap.createMap()
    mainKing = king(0, 0, 100, 1, 3)
    texture, heightTexture, maxWidthTexture = getTexture("../textures/king.txt")
    mainKing.assignHeight(heightTexture)
    mainKing.assignmaxWidth(maxWidthTexture)
    mainKing.assignInitialPosition(mainMap, texture)
    mainMap.drawMap()
    while gameStatus == "playing":
        os.system("cls" if os.name == "nt" else "clear")
        mainMap.drawMap()
        print(mainKing.currPositionX, mainKing.currPositionY)
        print(mainKing.currPositionX + mainKing.maxWidth, mainKing.currPositionY + mainKing.height)
        ch = input_to(Get())
        if ch == "w" or ch == "a" or ch == "s" or ch == "d":
            mainKing.move(ch, mainMap, texture)
        elif ch == "q":
            gameStatus = "quit"
