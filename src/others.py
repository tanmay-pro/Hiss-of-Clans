from src.map import *
from src.buildings import *
from src.movingObjects import *

def getTexture(fileName):
    width = 0
    height = 0
    texture = []
    with open (fileName, 'r') as f:
        allLines = f.readlines()
        for everyLine in allLines:
            width = max(width, len(everyLine))
            texture.append(everyLine)
            height+=1
    return allLines, height, width
        
class spawningPoint:
    def __init__(self, x, y):
        self.positionX = x
        self.positionY = y

def getSwordPosition(posX, posY):
    posY += 1
    posX += 4
    return posX, posY

def checkGameStatus(mainMap, mainTownHall, arrayHuts, arrayCannons, mainKing, arrayBarbarians):
    gameLost = True
    gameWon = True
    if not mainTownHall.isDestroyed:
        gameWon = False
    for everyHut in arrayHuts:
        if not everyHut.isDestroyed:
            gameWon = False
    for everyCannon in arrayCannons:
        if not everyCannon.isDestroyed:
            gameWon = False
    if not mainKing.isDead:
        gameLost = False
    for everyBarbarian in arrayBarbarians:
        if not everyBarbarian.isDead:
            gameLost = False
    if gameLost and not gameWon:
        return 0
    if gameWon and not gameLost:
        return 1
    else:
        return 2