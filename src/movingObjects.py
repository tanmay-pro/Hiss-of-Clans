from re import S
from src.spells import *
from src.map import *
from src.others import *
from colorama import Fore, Back, Style

class movingObject:

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
        self.isDead = False
        self.isKing = False
        # self.currColor = None

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
                    mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary -
                                                      self.startPositionY][j-mainMap.horizontalBoundary - self.startPositionX]
                    mainMap.grid[i][j] = Fore.BLACK + \
                        Back.GREEN + mainMap.grid[i][j]
                    if not self.isKing:
                        mainMap.grid[i][j] = Fore.BLACK + Back.GREEN + \
                            Style.BRIGHT + mainMap.grid[i][j] + Style.RESET_ALL    

    def updatePosition(self, mainMap):
        for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
            for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":
                    mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary -
                                                      self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX]
                    mainMap.grid[i][j] = Fore.BLACK + \
                        Back.GREEN + mainMap.grid[i][j]
                    # self.currColor = Fore.BLACK + Back.GREEN
                    if not self.isKing:
                        # self.currColor = Fore.BLACK + Back.GREEN + Style.BRIGHT
                        mainMap.grid[i][j] = Fore.BLACK + Back.GREEN + \
                            Style.BRIGHT + mainMap.grid[i][j] + Style.RESET_ALL

    def clearObject(self, mainMap):
        for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
            for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":
                    mainMap.grid[i][j] = Back.GREEN + Fore.GREEN + " "

    def castSpell(self, cast):
        self.damage *= cast.damageEffect
        self.movSpeed *= cast.speedEffect
        self.currHealth *= cast.healthEffect
        if(self.currHealth > self.fullHealth):
            self.currHealth = self.fullHealth


class king(movingObject):

    def __init__(self, startX, startY, health, speed, damage):
        super().__init__(startX, startY, health, speed, damage)
        self.previousMove = None

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

    def attack(self, mainMap, townHall, huts, walls, cannons, towers):
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
        for everyTower in towers:
            if not everyTower.isDestroyed:
                if everyTower.checkUnit(mainMap, attackX, attackY):
                    everyTower.deductHealth(self.damage, mainMap)

    def attackMajor(self, mainMap, townHall, huts, walls, cannons, towers, AXE_RANGE):
        attackX = self.currPositionX
        attackY = self.currPositionY

        if not townHall.isDestroyed:
            if townHall.checkIfUnitInRange(mainMap, attackX, attackY, AXE_RANGE):
                townHall.deductHealth(self.damage, mainMap)
        for everyHut in huts:
            if not everyHut.isDestroyed:
                if everyHut.checkIfUnitInRange(mainMap, attackX, attackY, AXE_RANGE):
                    everyHut.deductHealth(self.damage, mainMap)
        for everyWall in walls:
            if not everyWall.isDestroyed:
                if everyWall.checkIfUnitInRange(mainMap, attackX, attackY, AXE_RANGE):
                    everyWall.deductHealth(self.damage, mainMap)
        for everyCannon in cannons:
            if not everyCannon.isDestroyed:
                if everyCannon.checkIfUnitInRange(mainMap, attackX, attackY, AXE_RANGE):
                    everyCannon.deductHealth(self.damage, mainMap)
        for everyTower in towers:
            if not everyTower.isDestroyed:
                if everyTower.checkIfUnitInRange(mainMap, attackX, attackY, AXE_RANGE):
                    everyTower.deductHealth(self.damage, mainMap)


class archerQueen(movingObject):

    def __init__(self, startX, startY, health, speed, damage):
        super().__init__(startX, startY, health, speed, damage)
        self.previousMove = None
        self.aoeRange = 5
        self.aoeRangeMajor = 9

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
        print("Queen Health = " + str(self.currHealth))

    def performAttack(self, mainMap, townHall, huts, walls, cannons, towers, posX, posY):
        if not townHall.isDestroyed:
            if townHall.checkIfUnitInRange(mainMap, posX, posY, self.aoeRange):
                townHall.deductHealth(self.damage, mainMap)
        for everyHut in huts:
            if not everyHut.isDestroyed:
                if everyHut.checkIfUnitInRange(mainMap, posX, posY, self.aoeRange):
                    everyHut.deductHealth(self.damage, mainMap)
        for everyWall in walls:
            if not everyWall.isDestroyed:
                if everyWall.checkIfUnitInRange(mainMap, posX, posY, self.aoeRange):
                    everyWall.deductHealth(self.damage, mainMap)
        for everyCannon in cannons:
            if not everyCannon.isDestroyed:
                if everyCannon.checkIfUnitInRange(mainMap, posX, posY, self.aoeRange):
                    everyCannon.deductHealth(self.damage, mainMap)
        for everyTower in towers:
            if not everyTower.isDestroyed:
                if everyTower.checkIfUnitInRange(mainMap, posX, posY, self.aoeRange):
                    everyTower.deductHealth(self.damage, mainMap)

    def performAttackMajor(self, mainMap, townHall, huts, walls, cannons, towers, posX, posY):
        if not townHall.isDestroyed:
            if townHall.checkIfUnitInRange(mainMap, posX, posY, self.aoeRangeMajor):
                townHall.deductHealth(self.damage, mainMap)
        for everyHut in huts:
            if not everyHut.isDestroyed:
                if everyHut.checkIfUnitInRange(mainMap, posX, posY, self.aoeRangeMajor):
                    everyHut.deductHealth(self.damage, mainMap)
        for everyWall in walls:
            if not everyWall.isDestroyed:
                if everyWall.checkIfUnitInRange(mainMap, posX, posY, self.aoeRangeMajor):
                    everyWall.deductHealth(self.damage, mainMap)
        for everyCannon in cannons:
            if not everyCannon.isDestroyed:
                if everyCannon.checkIfUnitInRange(mainMap, posX, posY, self.aoeRangeMajor):
                    everyCannon.deductHealth(self.damage, mainMap)
        for everyTower in towers:
            if not everyTower.isDestroyed:
                if everyTower.checkIfUnitInRange(mainMap, posX, posY, self.aoeRangeMajor):
                    everyTower.deductHealth(self.damage, mainMap)

    def attack(self, mainMap, townHall, huts, walls, cannons, towers):
        attackX = self.currPositionX
        attackY = self.currPositionY

        if self.previousMove == "d":
            attackX += 8
        elif self.previousMove == "s":
            attackY += 8
        elif self.previousMove == "a":
            attackX -= 8
        elif self.previousMove == "w":
            attackY -= 8
        
        # If we want to attack irrespective of building present 8 tiles far

        self.performAttack(mainMap, townHall, huts, walls, cannons, towers, attackX, attackY)

        # If we want to attack in AoE only if building is present 8 tiles far, then use below code 


        # if not townHall.isDestroyed:
        #     if townHall.checkUnit(mainMap, attackX, attackY):
        #         # townHall.deductHealth(self.damage, mainMap)
        #         self.performAttack(mainMap, townHall, huts,
        #                            walls, cannons, towers, attackX, attackY)
        # for everyHut in huts:
        #     if not everyHut.isDestroyed:
        #         if everyHut.checkUnit(mainMap, attackX, attackY):
        #             # everyHut.deductHealth(self.damage, mainMap)
        #             self.performAttack(mainMap, townHall, huts,
        #                                walls, cannons, towers, attackX, attackY)
        #             break

        # for everyWall in walls:
        #     if not everyWall.isDestroyed:
        #         if everyWall.checkUnit(mainMap, attackX, attackY):
        #             # everyWall.deductHealth(self.damage, mainMap)
        #             self.performAttack(mainMap, townHall, huts,
        #                                walls, cannons, towers, attackX, attackY)
        #             break

        # for everyCannon in cannons:
        #     if not everyCannon.isDestroyed:
        #         if everyCannon.checkUnit(mainMap, attackX, attackY):
        #             # everyCannon.deductHealth(self.damage, mainMap)
        #             self.performAttack(mainMap, townHall, huts,
        #                                walls, cannons, towers, attackX, attackY)
        #             break

        # for everyTower in towers:
        #     if not everyTower.isDestroyed:
        #         if everyTower.checkUnit(mainMap, attackX, attackY):
        #             # everyTower.deductHealth(self.damage, mainMap)
        #             self.performAttack(mainMap, townHall, huts,
        #                                walls, cannons, towers, attackX, attackY)
        #             break

    def attackMajor(self, mainMap, townHall, huts, walls, cannons, towers):
        attackX = self.currPositionX
        attackY = self.currPositionY

        if self.previousMove == "d":
            attackX += 16
        elif self.previousMove == "s":
            attackY += 16
        elif self.previousMove == "a":
            attackX -= 16
        elif self.previousMove == "w":
            attackY -= 16
        
        # If we want to attack irrespective of building present 8 tiles far

        self.performAttackMajor(mainMap, townHall, huts, walls, cannons, towers, attackX, attackY)
    

class barbarian(movingObject):

    def __init__(self, startX, startY, health, speed, damage):
        super().__init__(startX, startY, health, speed, damage)

    def move(self, mainMap, townHall, huts, walls, cannons, towers):
        dist = {}
        if not townHall.isDestroyed:
            townHall.getDistances(
                mainMap, dist, self.currPositionX, self.currPositionY)
        for everyHut in huts:
            if not everyHut.isDestroyed:
                everyHut.getDistances(
                    mainMap, dist, self.currPositionX, self.currPositionY)
        for everyCannon in cannons:
            if not everyCannon.isDestroyed:
                everyCannon.getDistances(
                    mainMap, dist, self.currPositionX, self.currPositionY)
        for everyTower in towers:
            if not everyTower.isDestroyed:
                everyTower.getDistances(
                    mainMap, dist, self.currPositionX, self.currPositionY)

        minDist = 1e7
        minDistX = -1
        minDistY = -1

        for key, value in dist.items():
            if value < minDist:
                minDist = value
                array = key.split(".")
                minDistY = int(array[0])
                minDistX = int(array[1])
        self.decideDirection(mainMap, minDistX, minDistY)

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

        if not changeX and not changeY:
            if posX > self.currPositionX + mainMap.horizontalBoundary:
                temp = mainMap.grid[self.currPositionY + mainMap.verticalBoundary][self.currPositionX +
                                                                                   mainMap.horizontalBoundary + self.maxWidth]
                temp = temp[-5]
                if temp == "B":
                    self.currPositionX += 1

            if posX < self.currPositionX + mainMap.horizontalBoundary:
                temp = mainMap.grid[self.currPositionY +
                                    mainMap.verticalBoundary][self.currPositionX + mainMap.horizontalBoundary - 1]
                temp = temp[-5]
                if temp == "B":
                    self.currPositionX -= 1

            if posY > self.currPositionY + mainMap.verticalBoundary:
                temp = mainMap.grid[self.currPositionY + mainMap.verticalBoundary +
                                    self.height][self.currPositionX + mainMap.horizontalBoundary]
                temp = temp[-5]
                if temp == "B":
                    self.currPositionY += 1

            if posY < self.currPositionY + mainMap.verticalBoundary:
                temp = mainMap.grid[self.currPositionY + mainMap.verticalBoundary -
                                    1][self.currPositionX + mainMap.horizontalBoundary]
                temp = temp[-5]
                if temp == "B":
                    self.currPositionY -= 1

        self.updatePosition(mainMap)

    def deductHealth(self, damage, mainMap):
        self.currHealth -= damage
        self.changeColor(mainMap)
        if self.currHealth <= 0:
            self.isDead = True
            self.clearObject(mainMap)

    def changeColor(self, mainMap):
        blocks = int(self.currHealth/self.fullHealth * 10)
        if blocks <= 2:
            for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
                for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                    if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":
                        mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary -
                                                          self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX]
                        # mainMap.grid[i][j] = Fore.RED + Back.GREEN + mainMap.grid[i][j]
                        # self.currColor = Fore.BLACK + Back.GREEN + Style.DIM
                        mainMap.grid[i][j] = Fore.BLACK + Back.GREEN + \
                            Style.DIM + mainMap.grid[i][j] + Style.RESET_ALL

        if blocks <= 5 and blocks > 2:
            for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
                for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                    if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":
                        mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary -
                                                          self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX]
                        # mainMap.grid[i][j] = Fore.YELLOW + Back.GREEN + mainMap.grid[i][j]
                        # self.currColor = Fore.BLACK + Back.GREEN + Style.NORMAL
                        mainMap.grid[i][j] = Fore.BLACK + Back.GREEN + \
                            Style.NORMAL + mainMap.grid[i][j] + Style.RESET_ALL


        if blocks <= 10 and blocks > 5:
            for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
                for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                    if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":
                        mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary -
                                                          self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX]
                        # mainMap.grid[i][j] = Fore.BLACK + Back.GREEN + mainMap.grid[i][j]
                        # self.currColor = Fore.BLACK + Back.GREEN + Style.BRIGHT
                        mainMap.grid[i][j] = Fore.BLACK + Back.GREEN + \
                            Style.BRIGHT + mainMap.grid[i][j] + Style.RESET_ALL


    def attack(self, mainMap, townHall, huts, walls, cannons, towers):
        hasAttacked = False
        attackX = self.currPositionX
        attackY = self.currPositionY
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
        for everyTower in towers:
            if not everyTower.isDestroyed:
                if everyTower.checkUnit(mainMap, attackX, attackY):
                    everyTower.deductHealth(self.damage, mainMap)
                    hasAttacked = True
        if hasAttacked:
            return True

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
        for everyTower in towers:
            if not everyTower.isDestroyed:
                if everyTower.checkUnit(mainMap, attackX, attackY):
                    everyTower.deductHealth(self.damage, mainMap)
                    hasAttacked = True

        if hasAttacked:
            return True

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
        for everyTower in towers:
            if not everyTower.isDestroyed:
                if everyTower.checkUnit(mainMap, attackX, attackY):
                    everyTower.deductHealth(self.damage, mainMap)
                    hasAttacked = True

        if hasAttacked:
            return True

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
        for everyTower in towers:
            if not everyTower.isDestroyed:
                if everyTower.checkUnit(mainMap, attackX, attackY):
                    everyTower.deductHealth(self.damage, mainMap)
                    hasAttacked = True
        
        if hasAttacked:
            return True
        
        return False


class archer(movingObject):

    def __init__(self, startX, startY, health, speed, damage, range):
        super().__init__(startX, startY, health, speed, damage)
        self.range = range

    def move(self, mainMap, townHall, huts, walls, cannons, towers):
        dist = {}
        if not townHall.isDestroyed:
            townHall.getDistances(
                mainMap, dist, self.currPositionX, self.currPositionY)
        for everyHut in huts:
            if not everyHut.isDestroyed:
                everyHut.getDistances(
                    mainMap, dist, self.currPositionX, self.currPositionY)
        for everyCannon in cannons:
            if not everyCannon.isDestroyed:
                everyCannon.getDistances(
                    mainMap, dist, self.currPositionX, self.currPositionY)
        for everyTower in towers:
            if not everyTower.isDestroyed:
                everyTower.getDistances(
                    mainMap, dist, self.currPositionX, self.currPositionY)

        minDist = 1e7
        minDistX = -1
        minDistY = -1

        for key, value in dist.items():
            if value < minDist:
                minDist = value
                array = key.split(".")
                minDistY = int(array[0])
                minDistX = int(array[1])
        self.decideDirection(mainMap, minDistX, minDistY, walls)

    def decideDirection(self, mainMap, posX, posY, walls):
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

        if not changeX and not changeY:
            if posX > self.currPositionX + mainMap.horizontalBoundary:
                temp = mainMap.grid[self.currPositionY + mainMap.verticalBoundary][self.currPositionX +
                                                                                   mainMap.horizontalBoundary + self.maxWidth]
                temp = temp[-5]
                if temp == "A":
                    self.currPositionX += 1
                    changeX = True

            if posX < self.currPositionX + mainMap.horizontalBoundary:
                temp = mainMap.grid[self.currPositionY +
                                    mainMap.verticalBoundary][self.currPositionX + mainMap.horizontalBoundary - 1]
                temp = temp[-5]
                if temp == "A":
                    self.currPositionX -= 1
                    changeX = True

            if posY > self.currPositionY + mainMap.verticalBoundary:
                temp = mainMap.grid[self.currPositionY + mainMap.verticalBoundary +
                                    self.height][self.currPositionX + mainMap.horizontalBoundary]
                temp = temp[-5]
                if temp == "A":
                    self.currPositionY += 1
                    changeY = True

            if posY < self.currPositionY + mainMap.verticalBoundary:
                temp = mainMap.grid[self.currPositionY + mainMap.verticalBoundary -
                                    1][self.currPositionX + mainMap.horizontalBoundary]
                temp = temp[-5]
                if temp == "A":
                    self.currPositionY -= 1
                    changeY = True

        if not changeX and not changeY:
            self.imitateBarbarianattack(mainMap, walls)

        self.updatePosition(mainMap)

    def attack(self, mainMap, townHall, huts, walls, cannons, towers):
        attackX = self.currPositionX
        attackY = self.currPositionY
        attackDone = False

        for everyCannon in cannons:
                if not everyCannon.isDestroyed:
                    if everyCannon.checkIfUnitInRange(mainMap, attackX, attackY, self.range):
                        everyCannon.deductHealth(self.damage, mainMap)
                        attackDone = True
                        break

        if not attackDone:
            for everyTower in towers:
                if not everyTower.isDestroyed:
                    if everyTower.checkIfUnitInRange(mainMap, attackX, attackY, self.range):
                        everyTower.deductHealth(self.damage, mainMap)
                        attackDone = True
                        break
        
        if not attackDone:
            if not townHall.isDestroyed:
                if townHall.checkIfUnitInRange(mainMap, attackX, attackY, self.range):
                    townHall.deductHealth(self.damage, mainMap)
                    attackDone = True
        
        if not attackDone:
            for everyHut in huts:
                if not everyHut.isDestroyed:
                    if everyHut.checkIfUnitInRange(mainMap, attackX, attackY, self.range):
                        everyHut.deductHealth(self.damage, mainMap)
                        attackDone = True
                        break
        
        if not attackDone:
            return False
        else:
            return True

    def imitateBarbarianattack(self, mainMap, walls):
        # attackX, attackY = getSwordPosition(self.currPositionX, self.currPositionY)
        hasAttacked = False
        attackX = self.currPositionX
        attackY = self.currPositionY

        # mainMap.backGrid[attackX + mainMap.horizontalBoundary][attackY + mainMap.verticalBoundary] = "S"
        attackX += 1
        for everyWall in walls:
            if not everyWall.isDestroyed:
                if everyWall.checkUnit(mainMap, attackX, attackY):
                    everyWall.deductHealth(self.damage, mainMap)
                    hasAttacked = True
        if hasAttacked:
            return

        attackX -= 2

        for everyWall in walls:
            if not everyWall.isDestroyed:
                if everyWall.checkUnit(mainMap, attackX, attackY):
                    everyWall.deductHealth(self.damage, mainMap)
                    hasAttacked = True

        if hasAttacked:
            return

        attackX += 1
        attackY += 1

        for everyWall in walls:
            if not everyWall.isDestroyed:
                if everyWall.checkUnit(mainMap, attackX, attackY):
                    everyWall.deductHealth(self.damage, mainMap)
                    hasAttacked = True
        if hasAttacked:
            return

        attackY -= 2

        for everyWall in walls:
            if not everyWall.isDestroyed:
                if everyWall.checkUnit(mainMap, attackX, attackY):
                    everyWall.deductHealth(self.damage, mainMap)
                    hasAttacked = True

    def deductHealth(self, damage, mainMap):
        self.currHealth -= damage
        self.changeColor(mainMap)
        if self.currHealth <= 0:
            self.isDead = True
            self.clearObject(mainMap)

    def changeColor(self, mainMap):
        blocks = int(self.currHealth/self.fullHealth * 10)
        if blocks <= 2:
            for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
                for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                    if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":
                        mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary -
                                                          self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX]
                        # mainMap.grid[i][j] = Fore.RED + Back.GREEN + mainMap.grid[i][j]
                        # self.currColor = Fore.BLACK + Back.GREEN + Style.DIM
                        mainMap.grid[i][j] = Fore.BLACK + Back.GREEN + \
                            Style.DIM + mainMap.grid[i][j] + Style.RESET_ALL


        if blocks <= 5 and blocks > 2:
            for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
                for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                    if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":
                        mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary -
                                                          self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX]
                        # mainMap.grid[i][j] = Fore.YELLOW + Back.GREEN + mainMap.grid[i][j]
                        # self.currColor = Fore.BLACK + Back.GREEN + Style.NORMAL
                        mainMap.grid[i][j] = Fore.BLACK + Back.GREEN + \
                            Style.NORMAL + mainMap.grid[i][j] + Style.RESET_ALL

        if blocks <= 10 and blocks > 5:
            for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
                for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                    if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":
                        mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary -
                                                          self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX]
                        # mainMap.grid[i][j] = Fore.BLACK + Back.GREEN + mainMap.grid[i][j]
                        # self.currColor = Fore.BLACK + Back.GREEN + Style.BRIGHT
                        mainMap.grid[i][j] = Fore.BLACK + Back.GREEN + \
                            Style.BRIGHT + mainMap.grid[i][j] + Style.RESET_ALL


class balloon(movingObject):

    def __init__(self, startX, startY, health, speed, damage):
        super().__init__(startX, startY, health, speed, damage)

    def deductHealth(self, damage, mainMap):
        self.currHealth -= damage
        self.changeColorAir(mainMap)
        if self.currHealth <= 0:
            self.isDead = True
            self.clearObjectAir(mainMap)

    def clearObjectAir(self, mainMap):
        for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
            for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":
                    mainMap.airGrid[i][j] = " "

    def assignPositionAir(self, mainMap):
        for i in range(mainMap.verticalBoundary + self.startPositionY, self.height + mainMap.verticalBoundary + self.startPositionY):
            for j in range(mainMap.horizontalBoundary + self.startPositionX, len(self.texture[i - mainMap.verticalBoundary - self.startPositionY]) + mainMap.horizontalBoundary + self.startPositionX):
                if self.texture[i-mainMap.verticalBoundary - self.startPositionY][j-mainMap.horizontalBoundary - self.startPositionX] != "\n":
                    mainMap.airGrid[i][j] = self.texture[i-mainMap.verticalBoundary - self.startPositionY][j-mainMap.horizontalBoundary - self.startPositionX]
                    mainMap.airGrid[i][j] = Fore.BLACK + Back.GREEN + mainMap.airGrid[i][j]
                    mainMap.airGrid[i][j] = Fore.BLACK + Back.GREEN + Style.BRIGHT + mainMap.airGrid[i][j] + Style.RESET_ALL 

    def updatePositionAir(self, mainMap):
        for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
            for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":
                    mainMap.airGrid[i][j] = self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX]
                    mainMap.airGrid[i][j] = Fore.BLACK + Back.GREEN + mainMap.airGrid[i][j]
                    mainMap.airGrid[i][j] = Fore.BLACK + Back.GREEN + Style.BRIGHT + mainMap.airGrid[i][j] + Style.RESET_ALL   

    def changeColorAir(self, mainMap):
        blocks = int(self.currHealth/self.fullHealth * 10)
        if blocks <= 2:
            for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
                for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                    if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":
                        mainMap.airGrid[i][j] = self.texture[i-mainMap.verticalBoundary -
                                                          self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX]
                        mainMap.airGrid[i][j] = Fore.BLACK + Back.GREEN + \
                            Style.DIM + mainMap.airGrid[i][j] + Style.RESET_ALL

        if blocks <= 5 and blocks > 2:
            for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
                for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                    if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":
                        mainMap.airGrid[i][j] = self.texture[i-mainMap.verticalBoundary -
                                                          self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX]
                        mainMap.airGrid[i][j] = Fore.BLACK + Back.GREEN + \
                            Style.NORMAL + mainMap.airGrid[i][j] + Style.RESET_ALL

        if blocks <= 10 and blocks > 5:
            for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
                for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                    if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":
                        mainMap.airGrid[i][j] = self.texture[i-mainMap.verticalBoundary -
                                                          self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX]
                        mainMap.airGrid[i][j] = Fore.BLACK + Back.GREEN + \
                            Style.BRIGHT + mainMap.airGrid[i][j] + Style.RESET_ALL

    def move(self, mainMap, townHall, huts, walls, cannons, towers):

        allDefensiveDestroyed = True
        for everyCannon in cannons:
            if not everyCannon.isDestroyed:
                allDefensiveDestroyed = False
                break
        for everyTower in towers:
            if not everyTower.isDestroyed:
                allDefensiveDestroyed = False
                break

        dist = {}

        if allDefensiveDestroyed:
            if not townHall.isDestroyed:
                townHall.getDistances(
                    mainMap, dist, self.currPositionX, self.currPositionY)
            for everyHut in huts:
                if not everyHut.isDestroyed:
                    everyHut.getDistances(
                        mainMap, dist, self.currPositionX, self.currPositionY)
        else:
            for everyCannon in cannons:
                if not everyCannon.isDestroyed:
                    everyCannon.getDistances(
                        mainMap, dist, self.currPositionX, self.currPositionY)
            for everyTower in towers:
                if not everyTower.isDestroyed:
                    everyTower.getDistances(
                        mainMap, dist, self.currPositionX, self.currPositionY)

        minDist = 1e7
        minDistX = -1
        minDistY = -1

        for key, value in dist.items():
            if value < minDist:
                minDist = value
                array = key.split(".")
                minDistY = int(array[0])
                minDistX = int(array[1])
        self.decideDirection(mainMap, minDistX, minDistY)

    def decideDirection(self, mainMap, posX, posY):
        self.clearObjectAir(mainMap)
        if posX > self.currPositionX + mainMap.horizontalBoundary and mainMap.grid[self.currPositionY + mainMap.verticalBoundary][self.currPositionX + mainMap.horizontalBoundary + self.maxWidth] != Back.YELLOW + Fore.YELLOW + " ":
            self.currPositionX += 1
        elif posX < self.currPositionX + mainMap.horizontalBoundary and mainMap.grid[self.currPositionY + mainMap.verticalBoundary][self.currPositionX + mainMap.horizontalBoundary - 1] != Back.YELLOW + Fore.YELLOW + " ":
            self.currPositionX -= 1
        if posY > self.currPositionY + mainMap.verticalBoundary and mainMap.grid[self.currPositionY + mainMap.verticalBoundary + self.height][self.currPositionX + mainMap.horizontalBoundary] != Back.YELLOW + Fore.YELLOW + " ":
            self.currPositionY += 1
        elif posY < self.currPositionY + mainMap.verticalBoundary and mainMap.grid[self.currPositionY + mainMap.verticalBoundary - 1][self.currPositionX + mainMap.horizontalBoundary] != Back.YELLOW + Fore.YELLOW + " ":
            self.currPositionY -= 1
        self.updatePositionAir(mainMap)

    def attack(self, mainMap, townHall, huts, walls, cannons, towers):
        attackX = self.currPositionX
        attackY = self.currPositionY
        hasAttacked = False

        for everyCannon in cannons:
            if not everyCannon.isDestroyed:
                if everyCannon.checkUnit(mainMap, attackX, attackY):
                    everyCannon.deductHealth(self.damage, mainMap)
                    hasAttacked = True

        if not hasAttacked:
            for everyTower in towers:
                if not everyTower.isDestroyed:
                    if everyTower.checkUnit(mainMap, attackX, attackY):
                        everyTower.deductHealth(self.damage, mainMap)
                        hasAttacked = True

        if not hasAttacked:
            if not townHall.isDestroyed:
                if townHall.checkUnit(mainMap, attackX, attackY):
                    townHall.deductHealth(self.damage, mainMap)
                    hasAttacked = True

        if not hasAttacked:
            for everyHut in huts:
                if not everyHut.isDestroyed:
                    if everyHut.checkUnit(mainMap, attackX, attackY):
                        everyHut.deductHealth(self.damage, mainMap)
                        hasAttacked = True
        
        if hasAttacked:
            return True
        else:
            return False