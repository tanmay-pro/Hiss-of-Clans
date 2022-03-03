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
    
    mainMap = map(120, 30, 2, 1)
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
    
    arrayHuts = []
    hut1 = hut(10, 10, 100)
    hut2 = hut(20, 10, 100)
    hut3 = hut(10, 15, 100)
    hut4 = hut(20, 15, 100)
    hut5 = hut(20, 20, 100)
    arrayHuts.append(hut1)
    arrayHuts.append(hut2)
    arrayHuts.append(hut3)        
    arrayHuts.append(hut4)    
    arrayHuts.append(hut5)    
    texture, heightTexture, maxWidthTexture = getTexture("../textures/hut.txt")
    for hut in arrayHuts:
        hut.assignHeight(heightTexture)
        hut.assignmaxWidth(maxWidthTexture)
        hut.assignTexture(texture)
        hut.assignInitialPosition(mainMap) 
    
    arrayWalls = []

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
