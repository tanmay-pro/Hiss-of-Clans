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
from config import *

colorama.init(autoreset=True)
gameStatus = "playing"

if __name__ == "__main__":
    orig_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)

    mainMap = map(GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT, GAME_HORIZONTAL_BOUNDARY, GAME_VERTCIAL_BOUNDARY)
    mainMap.createMap()

    mainKing = king(KING_STARTING_X, KING_STARTING_Y, KING_HEALTH, KING_SPEED, KING_ATTACK)
    texture, heightTexture, maxWidthTexture = getTexture(
        "../textures/king.txt")
    mainKing.assignHeight(heightTexture)
    mainKing.assignmaxWidth(maxWidthTexture)
    mainKing.assignTexture(texture)
    mainKing.assignInitialPosition(mainMap)

    mainTownHall = townHall(TOWN_X_POSITION, TOWN_Y_POSITION, TOWN_HEALTH)
    texture, heightTexture, maxWidthTexture = getTexture(
        "../textures/townHall.txt")
    mainTownHall.assignHeight(heightTexture)
    mainTownHall.assignmaxWidth(maxWidthTexture)
    mainTownHall.assignTexture(texture)
    mainTownHall.assignPosition(mainMap)

    arrayHuts = []
    texture, heightTexture, maxWidthTexture = getTexture("../textures/hut.txt")
    for i in range(0, NUMBER_HUTS_IN_ROW):
        arrayHuts.append(hut(HUT_STARTING1, 10 + 6*i, 100))
    for i in range(0, NUMBER_HUTS_IN_ROW):
        arrayHuts.append(hut(HUT_STARTING2, 10 + 6*i, 100))
    for Hut in arrayHuts:
        Hut.assignHeight(heightTexture)
        Hut.assignmaxWidth(maxWidthTexture)
        Hut.assignTexture(texture)
        Hut.assignPosition(mainMap)

    arrayWalls = []
    texture, heightTexture, maxWidthTexture = getTexture(
        "../textures/wall.txt")
    for i in range(0, NUMBER_WALLS_Y):
        arrayWalls.append(wall(WALL_STARTING1X, WALL_STARTING1Y + i, 100))
    for i in range(0, NUMBER_WALLS_Y):
        arrayWalls.append(wall(WALL_STARTING2X, WALL_STARTING1Y + i, 100))
    for i in range(0, NUMBER_WALLS_X):
        arrayWalls.append(wall(WALL_STARTING1X + i, WALL_STARTING1Y, 100))
    for i in range(0, NUMBER_WALLS_X):
        arrayWalls.append(wall(WALL_STARTING1X + i, WALL_STARTING2Y, 100))

    for Wall in arrayWalls:
        Wall.assignHeight(heightTexture)
        Wall.assignmaxWidth(maxWidthTexture)
        Wall.assignTexture(texture)
        Wall.assignPosition(mainMap)

    arrayCannons = []
    texture, heightTexture, maxWidthTexture = getTexture(
        "../textures/cannon.txt")
    cannon1 = cannon(CANNON_1X, CANNON_1Y, CANNON_HEALTH, CANNON_DAMAGE, CANNON_RANGE)
    cannon2 = cannon(CANNON_2X, CANNON_2Y, CANNON_HEALTH, CANNON_DAMAGE, CANNON_RANGE)
    arrayCannons.append(cannon1)
    arrayCannons.append(cannon2)
    for Cannon in arrayCannons:
        Cannon.assignHeight(heightTexture)
        Cannon.assignmaxWidth(maxWidthTexture)
        Cannon.assignTexture(texture)
        Cannon.assignPosition(mainMap)

    mainMap.drawMap()

    while gameStatus == "playing":
        os.system("cls" if os.name == "nt" else "clear")
        mainMap.drawMap()
        print(mainTownHall.currHealth)
        ch = input_to(Get())
        if ch == "w" or ch == "a" or ch == "s" or ch == "d":
            mainKing.move(ch, mainMap)
        elif ch == "q":
            gameStatus = "quit"
        elif ch == " ":
            mainKing.attack(mainMap,0, mainTownHall, arrayHuts, arrayWalls, arrayCannons)
        sys.stdin.flush()
        sys.stdout.flush()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
