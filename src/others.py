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

def checkGameStatus(mainMap, mainTownHall, arrayHuts, arrayCannons, mainKing, arrayBarbarians, mainQueen, chosenKing):
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
    if chosenKing == 1 and not mainKing.isDead:
        gameLost = False
    elif chosenKing == 0 and not mainQueen.isDead:
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

def makeSpawningPoints(mainMap):
    spBarbarian = []
    sp1 = spawningPoint(5, 5)
    sp2 = spawningPoint(40, 2)
    sp3 = spawningPoint(90, 15)
    spBarbarian.append(sp1)
    spBarbarian.append(sp2)
    spBarbarian.append(sp3)
    spArcher = []
    sp1 = spawningPoint(5, 15)
    sp2 = spawningPoint(80, 2)
    sp3 = spawningPoint(45, 28)
    spArcher.append(sp1)
    spArcher.append(sp2)
    spArcher.append(sp3)
    spBalloon = []
    sp1 = spawningPoint(90, 25)
    sp2 = spawningPoint(100, 2)
    sp3 = spawningPoint(85, 20)
    spBalloon.append(sp1)
    spBalloon.append(sp2)
    spBalloon.append(sp3)
    return spBarbarian, spArcher, spBalloon