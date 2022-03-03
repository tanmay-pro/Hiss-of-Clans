from os import stat
from map import *

class movingObject:
    isdead = False
    
    def __init__(self, startX, startY, health, speed, damage):
        self.startPositionX = startX
        self.startPositionY = startY
        self.currPositionX = startX
        self.currPositionY = startY
        self.fullhealth = health
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
                    mainMap.grid[i][j] = Fore.RED + Back.GREEN + mainMap.grid[i][j] 
        

class king(movingObject): 
    def __init__(self, startX, startY, health, speed, damage):
        super().__init__(startX, startY, health, speed, damage)
    
    def move(self, pressedKey, mainMap):
        for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
            for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":                
                    mainMap.grid[i][j] = Back.GREEN + Fore.GREEN + " "
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
    
    def updatePosition(self, mainMap):
        for i in range(mainMap.verticalBoundary + self.currPositionY, self.height + mainMap.verticalBoundary + self.currPositionY):
            for j in range(mainMap.horizontalBoundary + self.currPositionX, len(self.texture[i - mainMap.verticalBoundary - self.currPositionY]) + mainMap.horizontalBoundary + self.currPositionX):
                if self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX] != "\n":     
                    mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary - self.currPositionY][j-mainMap.horizontalBoundary - self.currPositionX]
                    mainMap.grid[i][j] = Fore.RED + Back.GREEN + mainMap.grid[i][j] 
        
        

class barabarian(movingObject):
    def __init__(self, startX, startY, health, speed, damage):
        super().__init__(startX, startY, health, speed, damage)
