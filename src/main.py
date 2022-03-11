from multiprocessing.spawn import spawn_main
from matplotlib.pyplot import bar
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
import time

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
        arrayHuts.append(hut(HUT_STARTING1, HUT_STARTINGY + 6*i, HUT_HEALTH))
    for i in range(0, NUMBER_HUTS_IN_ROW):
        arrayHuts.append(hut(HUT_STARTING2, HUT_STARTINGY + 6*i, HUT_HEALTH))
    for Hut in arrayHuts:
        Hut.assignHeight(heightTexture)
        Hut.assignmaxWidth(maxWidthTexture)
        Hut.assignTexture(texture)
        Hut.assignPosition(mainMap)

    arrayWalls = []
    texture, heightTexture, maxWidthTexture = getTexture(
        "../textures/wall.txt")
    for i in range(0, NUMBER_WALLS_Y):
        arrayWalls.append(wall(WALL_STARTING1X, WALL_STARTING1Y + i, WALL_HEALTH))
    for i in range(0, NUMBER_WALLS_Y):
        arrayWalls.append(wall(WALL_STARTING2X, WALL_STARTING1Y + i, WALL_HEALTH))
    for i in range(0, NUMBER_WALLS_X):
        arrayWalls.append(wall(WALL_STARTING1X + i, WALL_STARTING1Y, WALL_HEALTH))
    for i in range(0, NUMBER_WALLS_X):
        arrayWalls.append(wall(WALL_STARTING1X + i, WALL_STARTING2Y, WALL_HEALTH))

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
    
    sp1 = spawningPoint(10, 10)
    sp2 = spawningPoint(10, 20)
    sp3 = spawningPoint(90, 15)
    
    arrayBarbarians = []
    texture, heightTexture, maxWidthTexture = getTexture("../textures/barbarian.txt")
    f = open("replayInputs.txt","w+")
    while gameStatus == "playing":
        startTime = time.time()
        os.system("cls" if os.name == "nt" else "clear")
        mainMap.drawMap()
        if not mainKing.isDead:
            mainKing.displayHealth()
        for everyBarbarian in arrayBarbarians:
            if not everyBarbarian.isDead: 
                everyBarbarian.move(mainMap, mainTownHall, arrayHuts, arrayWalls, arrayCannons)
                everyBarbarian.attack(mainMap, mainTownHall, arrayHuts, arrayWalls, arrayCannons)
        for everyCannon in arrayCannons:
            if not everyCannon.isDestroyed:
                everyCannon.attack(mainMap, mainKing, arrayBarbarians)
        if TIMEOUT_VAL > (time.time() - startTime):
            time.sleep(TIMEOUT_VAL - (time.time() - startTime))
        ch = input_to(Get())
        f.write(str(ch) + "\n")
        if ch == "w" or ch == "a" or ch == "s" or ch == "d":
            if not mainKing.isDead:
                mainKing.move(ch, mainMap)
        elif ch == "q":
            gameStatus = "quit"
        elif ch == " ":
            if not mainKing.isDead:
                mainKing.attack(mainMap, mainTownHall, arrayHuts, arrayWalls, arrayCannons)
        elif ch == "1" or ch=="2" or ch=="3":
            if ch == "1":
                barbarian1 = barbarian(sp1.positionX, sp1.positionY, BARBARIAN_HEALTH, BARBARIAN_SPEED, BARBARIAN_ATTACK)
            elif ch == "2":
                barbarian1 = barbarian(sp2.positionX, sp2.positionY, BARBARIAN_HEALTH, BARBARIAN_SPEED, BARBARIAN_ATTACK)
            elif ch=="3":
                barbarian1 = barbarian(sp3.positionX, sp3.positionY, BARBARIAN_HEALTH, BARBARIAN_SPEED, BARBARIAN_ATTACK)
            arrayBarbarians.append(barbarian1)
            barbarian1.assignHeight(heightTexture)
            barbarian1.assignmaxWidth(maxWidthTexture)
            barbarian1.assignTexture(texture)
            barbarian1.assignInitialPosition(mainMap)        
        elif ch == "r" or ch == "h":
            if ch == "r":
                Spell = spell(2, 2, 1)
            else:
                Spell = spell(1, 1, 1.5)
            if not mainKing.isDead:            
                mainKing.castSpell(Spell)
            for everyBarbarian in arrayBarbarians:
                if not everyBarbarian.isDead:
                    everyBarbarian.castSpell(Spell)

        returnVal = checkGameStatus(
                mainMap, mainTownHall, arrayHuts, arrayCannons, mainKing, arrayBarbarians)
        if returnVal == 0:
            gameStatus = "lost"
        elif returnVal == 1:
            gameStatus = "won"
        sys.stdin.flush()
        sys.stdout.flush()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
    f.close()
    if gameStatus == "won":
        os.system("cls" if os.name == "nt" else "clear")
        print("You won!")
    elif gameStatus == "lost":
        os.system("cls" if os.name == "nt" else "clear")
        print("You lost!")
    elif gameStatus == "quit":
        os.system("cls" if os.name == "nt" else "clear")
        print("You quit!")
