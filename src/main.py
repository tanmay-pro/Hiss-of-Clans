import numpy as np
import colorama
import time
import tty
import sys
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
    orig_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)
    
    mainMap = map(160, 40, 0, 0, 2, 1)
    mainMap.createMap()

    mainKing = king(0, 0, 100, 1, 3)
    texture, heightTexture, maxWidthTexture = getTexture("../textures/king.txt")
    mainKing.assignHeight(heightTexture)
    mainKing.assignmaxWidth(maxWidthTexture)
    mainKing.assignTexture(texture)
    mainKing.assignInitialPosition(mainMap)
    
    mainTownHall = townHall(70, 15, 100)
    texture, heightTexture, maxWidthTexture = getTexture("../textures/townHall.txt")
    mainTownHall.assignHeight(heightTexture)
    mainTownHall.assignmaxWidth(maxWidthTexture)
    mainTownHall.assignTexture(texture)
    mainTownHall.assignInitialPosition(mainMap)

    mainMap.drawMap()
    
    while gameStatus == "playing":
        os.system("cls" if os.name == "nt" else "clear")
        mainMap.drawMap()
        ch = input_to(Get())
        if ch == "w" or ch == "a" or ch == "s" or ch == "d":
            mainKing.move(ch, mainMap)
        elif ch == "q":
            gameStatus = "quit"
        sys.stdin.flush()
        sys.stdout.flush()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
