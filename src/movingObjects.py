from spells import *
from map import *
from others import *

class movingObject:
    isDead = False
    isKing = False

    def __init__(self, startX, startY, health, speed, damage):
        self.startPositionX = startX
        self.startPositionY = startY
        self.currPositionX = startX
        self.currPositionY = startY
        self.fullHealth = health
        self.currHealth = health
        self.hitpoints = health
        self.movSpeed = speed
        self.damage = damage

    def assignHeight(self, h):
        self.height = h
    
    def assignmaxWidth(self, w):
        self.maxWidth = w
    
    def assignTexture(self, texture):
        self.texture = texture

    def assignInitialPosition(self, mainMap):
        for i in range(mainMap.verticalBoundary + self.startPositionY, self.height + mainMap.verticalBoundary + self.startPositionY):
            for j in range(mainMap.horizontalBoundary + self.startPositionX, len(self.texture[i - mainMap.verticalBoundary - self.startPositionY]) + mainMap.horizontalBoundary + self.startPositionX):
                if self.texture[i-mainMap.verticalBoundary - self.startPositionY][j-mainMap.horizontalBoundary - self.startPositionX] != "\n":
                    mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary - self.startPositionY][j-mainMap.horizontalBoundary - self.startPositionX]
                    mainMap.grid[i][j] = Fore.BLACK + Back.GREEN + mainMap.grid[i][j] 
                    # if self.isKing:
                    #     mainMap.backGrid[i][j] = "K"
                    # else:
                    #     mainMap.backGrid[i][j] = "B"


    def updatePosition(self, mainMap):
        for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
            for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":     
                    mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX]
                    mainMap.grid[i][j] = Fore.BLACK + Back.GREEN + mainMap.grid[i][j] 
                    # if self.isKing:
                    #     mainMap.backGrid[i][j] = "K"
                    # else:
                    #     mainMap.backGrid[i][j] = "B"

    def clearObject(self, mainMap):
        for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
            for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":
                    mainMap.grid[i][j] = Back.GREEN + Fore.GREEN + " "
                    # if self.isKing:
                    #     mainMap.backGrid[i][j] = " "
                    # else:
                    #     mainMap.backGrid[i][j] = " " 
    
    def castSpell(self, cast):
        self.damage *= cast.damageEffect
        self.movSpeed *= cast.speedEffect
        self.currHealth *= cast.healthEffect
        if(self.currHealth > self.fullHealth):
            self.currHealth = self.fullHealth

class king(movingObject):     

    previousMove = None

    def __init__(self, startX, startY, health, speed, damage):
        super().__init__(startX, startY, health, speed, damage)
    
    def move(self, pressedKey, mainMap):
        self.clearObject(mainMap)
        self.previousMove = pressedKey
        if pressedKey == "w":
            status = True
            for i in range(self.currPositionX + mainMap.horizontalBoundary, self.currPositionX + mainMap.horizontalBoundary + self.maxWidth):
                if mainMap.grid[mainMap.verticalBoundary + self.currPositionY - 1][i] != Back.GREEN + Fore.GREEN + " ":
                    status = False
            if status:
                self.currPositionY -= 1
        elif pressedKey == "a":
            status = True
            for i in range(self.currPositionY + mainMap.verticalBoundary, self.currPositionY + mainMap.verticalBoundary + self.height):
                if mainMap.grid[i][self.currPositionX + mainMap.horizontalBoundary - 1] != Back.GREEN + Fore.GREEN + " ":
                    status = False
            if status:
                self.currPositionX -= 1
        elif pressedKey == "d":
            status = True
            for i in range(self.currPositionY + mainMap.verticalBoundary, self.currPositionY + mainMap.verticalBoundary + self.height):
                if mainMap.grid[i][self.currPositionX + mainMap.horizontalBoundary + self.maxWidth] != Back.GREEN + Fore.GREEN + " ":
                    status = False
            if status:
                self.currPositionX += 1
        elif pressedKey == "s":
            status = True
            for i in range(self.currPositionX + mainMap.horizontalBoundary, self.currPositionX + mainMap.horizontalBoundary + self.maxWidth):
                if mainMap.grid[mainMap.verticalBoundary + self.currPositionY + self.height][i] != Back.GREEN + Fore.GREEN + " ":
                    status = False
            if status:
                self.currPositionY += 1

        self.updatePosition(mainMap)

    def deductHealth(self, damage, mainMap):
        self.currHealth -= damage
        if self.currHealth <= 0:
            self.isDead = True
            self.clearObject(mainMap) 
    
    def displayHealth(self):
        blocks = int(self.currHealth / self.fullHealth * 10)
        healthBar = []
        if blocks > 0 and blocks <= 2:
            for i in range(blocks):
                healthBar.append(Fore.RED + Back.RED + " ")
        if blocks > 2 and blocks <= 5:
            for i in range(2):
                healthBar.append(Fore.RED + Back.RED + " ")
            for i in range(blocks-2):
                healthBar.append(Fore.YELLOW + Back.YELLOW + " ")
        if blocks > 5:
            for i in range(2):
                healthBar.append(Fore.RED + Back.RED + " ")
            for i in range(5):
                healthBar.append(Fore.YELLOW + Back.YELLOW + " ")    
            for i in range(blocks-5):
                healthBar.append(Fore.GREEN + Back.GREEN + " ")
        printMap = ""
        for r in range(len(healthBar)):
            printMap += healthBar[r]
        print(printMap)
        print("King Health = " + str(self.currHealth))

    def attack(self, mainMap, townHall, huts, walls, cannons):
        # attackX, attackY = getSwordPosition(self.currPositionX, self.currPositionY)
        attackX = self.currPositionX
        attackY = self.currPositionY

        if self.previousMove == "d":
            attackX += 1
        elif self.previousMove == "s":
            attackY += 1
        elif self.previousMove == "a":
            attackX -= 1
        elif self.previousMove == "w":
            attackY -= 1

        # mainMap.backGrid[attackX + mainMap.horizontalBoundary][attackY + mainMap.verticalBoundary] = "S"

        if not townHall.isDestroyed:
            if townHall.checkUnit(mainMap, attackX, attackY):
                townHall.deductHealth(self.damage, mainMap)
        for everyHut in huts:
            if not everyHut.isDestroyed:
                if everyHut.checkUnit(mainMap, attackX, attackY):
                    everyHut.deductHealth(self.damage, mainMap)
        for everyWall in walls:
            if not everyWall.isDestroyed:
                if everyWall.checkUnit(mainMap, attackX, attackY):
                    everyWall.deductHealth(self.damage, mainMap)
        for everyCannon in cannons:
            if not everyCannon.isDestroyed:
                if everyCannon.checkUnit(mainMap, attackX, attackY):
                    everyCannon.deductHealth(self.damage, mainMap)

    def attackMajor(self, mainMap, townHall, huts, walls, cannons):
        attackX = self.currPositionX
        attackY = self.currPositionY

        if not townHall.isDestroyed:
            if townHall.checkIfUnitInRange(mainMap, attackX, attackY):
                townHall.deductHealth(self.damage, mainMap)
        for everyHut in huts:
            if not everyHut.isDestroyed:
                if everyHut.checkIfUnitInRange(mainMap, attackX, attackY):
                    everyHut.deductHealth(self.damage, mainMap)
        for everyWall in walls:
            if not everyWall.isDestroyed:
                if everyWall.checkIfUnitInRange(mainMap, attackX, attackY):
                    everyWall.deductHealth(self.damage, mainMap)
        for everyCannon in cannons:
            if not everyCannon.isDestroyed:
                if everyCannon.checkIfUnitInRange(mainMap, attackX, attackY):
                    everyCannon.deductHealth(self.damage, mainMap)



class barbarian(movingObject):

    def __init__(self, startX, startY, health, speed, damage):
        super().__init__(startX, startY, health, speed, damage)
    
    def move(self, mainMap, townHall, huts, walls, cannons):
        dist = {}
        if not townHall.isDestroyed:
            townHall.getDistances(mainMap, dist, self.currPositionX, self.currPositionY)
        for everyHut in huts:
            if not everyHut.isDestroyed:
                everyHut.getDistances(mainMap, dist, self.currPositionX, self.currPositionY)
        for everyCannon in cannons:
            if not everyCannon.isDestroyed:
                everyCannon.getDistances(mainMap, dist, self.currPositionX, self.currPositionY)
        minDist = 1e7; minDistX = -1; minDistY = -1

        for key, value in dist.items():
            if value < minDist:
                minDist = value
                array = key.split(".")
                minDistY = int(array[0])
                minDistX = int(array[1])
        self.decideDirection(mainMap ,minDistX, minDistY)
        
    def decideDirection(self, mainMap, posX, posY):
        self.clearObject(mainMap)      
        changeX = False
        changeY = False
        if posX > self.currPositionX + mainMap.horizontalBoundary and mainMap.grid[self.currPositionY + mainMap.verticalBoundary][self.currPositionX + mainMap.horizontalBoundary + self.maxWidth] == Back.GREEN + Fore.GREEN + " ":
            self.currPositionX += 1
            changeX = True
        elif posX < self.currPositionX + mainMap.horizontalBoundary and mainMap.grid[self.currPositionY + mainMap.verticalBoundary][self.currPositionX + mainMap.horizontalBoundary - 1] == Back.GREEN + Fore.GREEN + " ":
            self.currPositionX -= 1
            changeX = True
        if posY > self.currPositionY + mainMap.verticalBoundary and mainMap.grid[self.currPositionY + mainMap.verticalBoundary + self.height][self.currPositionX + mainMap.horizontalBoundary] == Back.GREEN + Fore.GREEN + " ":
            self.currPositionY += 1
            changeY = True
        elif posY < self.currPositionY + mainMap.verticalBoundary and mainMap.grid[self.currPositionY + mainMap.verticalBoundary - 1][self.currPositionX + mainMap.horizontalBoundary] == Back.GREEN + Fore.GREEN + " ":
            self.currPositionY -= 1
            changeY = True

        self.updatePosition(mainMap)

    def deductHealth(self, damage, mainMap):
        self.currHealth -= damage
        self.changeColor(mainMap)
        if self.currHealth <= 0:
            self.isDead = True
            self.clearObject(mainMap) 

    def changeColor(self, mainMap):
        blocks = int(self.currHealth/self.fullHealth* 10)
        if blocks <= 2:
            for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
                for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                    if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":
                        mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX]
                        mainMap.grid[i][j] = Fore.RED + Back.GREEN + mainMap.grid[i][j]
    
        if blocks <= 5 and blocks > 2:
            for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
                for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                    if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":
                        mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX]
                        mainMap.grid[i][j] = Fore.YELLOW + Back.GREEN + mainMap.grid[i][j]

        if blocks <= 10 and blocks > 5:
            for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
                for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                    if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":
                        mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX]
                        mainMap.grid[i][j] = Fore.BLACK + Back.GREEN + mainMap.grid[i][j]
    
    def attack(self, mainMap, townHall, huts, walls, cannons):
        # attackX, attackY = getSwordPosition(self.currPositionX, self.currPositionY)
        hasAttacked = False
        attackX = self.currPositionX
        attackY = self.currPositionY
        
        # mainMap.backGrid[attackX + mainMap.horizontalBoundary][attackY + mainMap.verticalBoundary] = "S"
        attackX += 1

        if not townHall.isDestroyed:
            if townHall.checkUnit(mainMap, attackX, attackY):   
                townHall.deductHealth(self.damage, mainMap)
                hasAttacked = True
        for everyHut in huts:
            if not everyHut.isDestroyed:
                if everyHut.checkUnit(mainMap, attackX, attackY):
                    everyHut.deductHealth(self.damage, mainMap)
                    hasAttacked = True
        for everyWall in walls:
            if not everyWall.isDestroyed:
                if everyWall.checkUnit(mainMap, attackX, attackY):
                    everyWall.deductHealth(self.damage, mainMap)
                    hasAttacked = True
        for everyCannon in cannons:
            if not everyCannon.isDestroyed:
                if everyCannon.checkUnit(mainMap, attackX, attackY):
                    everyCannon.deductHealth(self.damage, mainMap) 
                    hasAttacked = True

        if hasAttacked:
            return 
        
        attackX -= 2

        if not townHall.isDestroyed:
            if townHall.checkUnit(mainMap, attackX, attackY):
                townHall.deductHealth(self.damage, mainMap)
                hasAttacked = True
        for everyHut in huts:
            if not everyHut.isDestroyed:
                if everyHut.checkUnit(mainMap, attackX, attackY):
                    everyHut.deductHealth(self.damage, mainMap)
                    hasAttacked = True
        for everyWall in walls:
            if not everyWall.isDestroyed:
                if everyWall.checkUnit(mainMap, attackX, attackY):
                    everyWall.deductHealth(self.damage, mainMap)
                    hasAttacked = True
        for everyCannon in cannons:
            if not everyCannon.isDestroyed:
                if everyCannon.checkUnit(mainMap, attackX, attackY):
                    everyCannon.deductHealth(self.damage, mainMap)
                    hasAttacked = True

        if hasAttacked:
            return

        attackX += 1
        attackY += 1

        if not townHall.isDestroyed:
            if townHall.checkUnit(mainMap, attackX, attackY):
                townHall.deductHealth(self.damage, mainMap)
                hasAttacked = True
        for everyHut in huts:
            if not everyHut.isDestroyed:
                if everyHut.checkUnit(mainMap, attackX, attackY):
                    everyHut.deductHealth(self.damage, mainMap)
                    hasAttacked = True
        for everyWall in walls:
            if not everyWall.isDestroyed:
                if everyWall.checkUnit(mainMap, attackX, attackY):
                    everyWall.deductHealth(self.damage, mainMap)
                    hasAttacked = True
        for everyCannon in cannons:
            if not everyCannon.isDestroyed:
                if everyCannon.checkUnit(mainMap, attackX, attackY):
                    everyCannon.deductHealth(self.damage, mainMap)
                    hasAttacked = True

        if hasAttacked:
            return

        attackY -= 2

        if not townHall.isDestroyed:
            if townHall.checkUnit(mainMap, attackX, attackY):
                townHall.deductHealth(self.damage, mainMap)
                hasAttacked = True
        for everyHut in huts:
            if not everyHut.isDestroyed:
                if everyHut.checkUnit(mainMap, attackX, attackY):
                    everyHut.deductHealth(self.damage, mainMap)
                    hasAttacked = True
        for everyWall in walls:
            if not everyWall.isDestroyed:
                if everyWall.checkUnit(mainMap, attackX, attackY):
                    everyWall.deductHealth(self.damage, mainMap)
                    hasAttacked = True
        for everyCannon in cannons:
            if not everyCannon.isDestroyed:
                if everyCannon.checkUnit(mainMap, attackX, attackY):
                    everyCannon.deductHealth(self.damage, mainMap)
                    hasAttacked = True
