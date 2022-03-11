from config import AXE_RANGE
from map import *
import math

class building:
    isDestroyed = False
    currHealth = None
    
    def __init__(self, x, y, hitpoints):
        self.positionX = x
        self.positionY = y
        self.fullHealth = hitpoints
        self.currHealth = hitpoints
        self.currForeColor = Fore.BLACK

    def assignHeight(self, h):
        self.height = h
    
    def assignmaxWidth(self, w):
        self.maxWidth = w
    
    def assignTexture(self, texture):
        self.texture = texture

    def assignPosition(self, mainMap):
        for i in range(mainMap.verticalBoundary + self.positionY, self.height + mainMap.verticalBoundary + self.positionY):
            for j in range(mainMap.horizontalBoundary + self.positionX, len(self.texture[i - mainMap.verticalBoundary - self.positionY]) + mainMap.horizontalBoundary + self.positionX):
                if self.texture[i-mainMap.verticalBoundary - self.positionY][j-mainMap.horizontalBoundary - self.positionX] != "\n":
                    mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary - self.positionY][j-mainMap.horizontalBoundary - self.positionX]
                    mainMap.grid[i][j] = Back.GREEN + Fore.BLACK + mainMap.grid[i][j]
                    self.currForeColor = Fore.BLACK
    
    def checkUnit(self, mainMap, posX, posY):
        present = False
        for i in range(mainMap.verticalBoundary + self.positionY, self.height + mainMap.verticalBoundary + self.positionY):
            for j in range(mainMap.horizontalBoundary + self.positionX, len(self.texture[i - mainMap.verticalBoundary - self.positionY]) + mainMap.horizontalBoundary + self.positionX):
                if i==posY + mainMap.verticalBoundary and j==posX + mainMap.horizontalBoundary:
                    present = True
        if present:
            return True
        else:
            return False
        
    def checkIfUnitInRange(self, mainMap, posX, posY):
        present = False
        for i in range(mainMap.verticalBoundary + self.positionY, self.height + mainMap.verticalBoundary + self.positionY):
            for j in range(mainMap.horizontalBoundary + self.positionX, len(self.texture[i - mainMap.verticalBoundary - self.positionY]) + mainMap.horizontalBoundary + self.positionX):
                if math.sqrt((i - posY)**2 + (j - posX)**2) <= AXE_RANGE:
                    present = True
        if present:
            return True
        else:
            return False

    def getDistances(self, mainMap, dist, posX, posY):
        for i in range(mainMap.verticalBoundary + self.positionY, self.height + mainMap.verticalBoundary + self.positionY):
            for j in range(mainMap.horizontalBoundary + self.positionX, len(self.texture[i - mainMap.verticalBoundary - self.positionY]) + mainMap.horizontalBoundary + self.positionX):
                dist[str(i) + '.' + str(j)] = math.sqrt((i - posY)**2 + (j - posX)**2)
        
    def deductHealth(self, damage, mainMap):
        self.currHealth -= damage
        self.changeColor(mainMap)
        self.checkDestroy(mainMap) 
    
    def checkDestroy(self, mainMap):                   
        if self.currHealth <= 0:
            self.isDestroyed = True
            self.destroy(mainMap)
    
    def destroy(self, mainMap):
        for i in range(mainMap.verticalBoundary + self.positionY, self.height + mainMap.verticalBoundary + self.positionY):
            for j in range(mainMap.horizontalBoundary + self.positionX, len(self.texture[i - mainMap.verticalBoundary - self.positionY]) + mainMap.horizontalBoundary + self.positionX):
                if self.texture[i-mainMap.verticalBoundary - self.positionY][j-mainMap.horizontalBoundary - self.positionX] != "\n":
                    mainMap.grid[i][j] = Back.GREEN + Fore.GREEN + " "
    
    def changeColor(self, mainMap):
        blocks = int(self.currHealth/self.fullHealth* 10)
        if blocks <= 2:
            for i in range(mainMap.verticalBoundary + self.positionY, self.height + mainMap.verticalBoundary + self.positionY):
                for j in range(mainMap.horizontalBoundary + self.positionX, len(self.texture[i - mainMap.verticalBoundary - self.positionY]) + mainMap.horizontalBoundary + self.positionX):
                    if self.texture[i-mainMap.verticalBoundary - self.positionY][j-mainMap.horizontalBoundary - self.positionX] != "\n":
                        mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary - self.positionY][j-mainMap.horizontalBoundary - self.positionX]
                        mainMap.grid[i][j] = Back.RED + self.currForeColor + mainMap.grid[i][j]
    
        if blocks <= 5 and blocks > 2:
            for i in range(mainMap.verticalBoundary + self.positionY, self.height + mainMap.verticalBoundary + self.positionY):
                for j in range(mainMap.horizontalBoundary + self.positionX, len(self.texture[i - mainMap.verticalBoundary - self.positionY]) + mainMap.horizontalBoundary + self.positionX):
                    if self.texture[i-mainMap.verticalBoundary - self.positionY][j-mainMap.horizontalBoundary - self.positionX] != "\n":
                        mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary - self.positionY][j-mainMap.horizontalBoundary - self.positionX]
                        mainMap.grid[i][j] = Back.YELLOW + self.currForeColor + mainMap.grid[i][j]

        if blocks <= 10 and blocks > 5:
            for i in range(mainMap.verticalBoundary + self.positionY, self.height + mainMap.verticalBoundary + self.positionY):
                for j in range(mainMap.horizontalBoundary + self.positionX, len(self.texture[i - mainMap.verticalBoundary - self.positionY]) + mainMap.horizontalBoundary + self.positionX):
                    if self.texture[i-mainMap.verticalBoundary - self.positionY][j-mainMap.horizontalBoundary - self.positionX] != "\n":
                        mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary - self.positionY][j-mainMap.horizontalBoundary - self.positionX]
                        mainMap.grid[i][j] = Back.GREEN + self.currForeColor + mainMap.grid[i][j]  
                
        
# Each building below shows inheritance
class cannon(building): 
    def __init__(self, x, y, hitpoints, damage, range):
        super().__init__(x, y, hitpoints)
        self.damage = damage
        self.range = range

    def attack(self, mainMap, mainKing, arrayBarbarians):
        attackX = self.positionX + mainMap.horizontalBoundary + 1
        attackY = self.positionY + mainMap.verticalBoundary + 1
        attackKing = False
        if not mainKing.isDead:
            distance = math.sqrt((attackX - mainKing.currPositionX)**2 + (attackY - mainKing.currPositionY)**2)
            if distance <= self.range:
                self.getColor(mainMap)
                mainKing.deductHealth(self.damage, mainMap)
                attackKing = True
        if not attackKing:
            for i in range(len(arrayBarbarians)):
                if not arrayBarbarians[i].isDead:
                    distance = math.sqrt((attackX - arrayBarbarians[i].currPositionX)**2 + (attackY - arrayBarbarians[i].currPositionY)**2)
                    if distance <= self.range:
                        self.getColor(mainMap)
                        arrayBarbarians[i].deductHealth(self.damage, mainMap)
                        break
    
    def getColor(self, mainMap):
        for i in range(mainMap.verticalBoundary + self.positionY, self.height + mainMap.verticalBoundary + self.positionY):
                    for j in range(mainMap.horizontalBoundary + self.positionX, len(self.texture[i - mainMap.verticalBoundary - self.positionY]) + mainMap.horizontalBoundary + self.positionX):
                        if self.texture[i-mainMap.verticalBoundary - self.positionY][j-mainMap.horizontalBoundary - self.positionX] != "\n":
                            mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary - self.positionY][j-mainMap.horizontalBoundary - self.positionX]
                            mainMap.grid[i][j] = Back.GREEN + Fore.BLUE + mainMap.grid[i][j]
                            self.currForeColor = Fore.BLUE


class wall(building):
    def __init__(self, x, y, hitpoints):
        super().__init__(x, y, hitpoints) # w and h should both be 1

class hut(building):
    def __init__(self, x, y, hitpoints):
        super().__init__(x, y, hitpoints)

class townHall(building):
    def __init__(self, x, y, hitpoints):
        super().__init__(x, y, hitpoints) ## w=4 and h=3 
