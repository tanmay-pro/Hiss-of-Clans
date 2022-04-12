import numpy as np
from colorama import Fore, Back, Style

class map:

    def __init__(self, cols, rows, h, v):
        self.rows = rows
        self.cols = cols
        self.horizontalBoundary = h
        self.verticalBoundary = v
        self.grid = []
        self.airGrid = []
    
    def createMap(self):
        for i in range(0, 2 * self.verticalBoundary + self.rows):
            row = []
            row2 = []
            if i < 0 + self.verticalBoundary:
                for j in range(0, 2 * self.horizontalBoundary + self.cols): 
                    row.append(Back.YELLOW + Fore.YELLOW +" ")
                    row2.append(" ")
            elif i >= 0 + self.verticalBoundary + self.rows:
                for j in range(0, 2 * self.horizontalBoundary + self.cols):
                    row.append(Back.YELLOW + Fore.YELLOW + " ")
                    row2.append(" ")
            else:
                for j in range(0, 2 * self.horizontalBoundary + self.cols):
                    if j < 0 + self.horizontalBoundary or j >= 0 + self.horizontalBoundary + self.cols:
                        row.append(Back.YELLOW + Fore.YELLOW + " ")
                        row2.append(" ")
                    else:
                        row.append(Back.GREEN + Fore.GREEN + " ")
                        row2.append(" ")
            self.grid.append(row)
            self.airGrid.append(row2)
            
    def drawMap(self):
        printMap = ""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                printMap += self.grid[r][c]
            printMap += '\n'    
        print('\033[H' + printMap)

    def drawMap2(self):
        printMap = ""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if self.airGrid[r][c] != " ":
                    printMap += self.airGrid[r][c]
                else:
                    printMap += self.grid[r][c]
            printMap += '\n'    
        print('\033[H' + printMap)

    def reconstructMap(self, townHall, huts, walls, cannons, towers, mainKing, mainQueen, arraybarbarians, arrayArchers, arrayBalloons):
        if not townHall.isDestroyed:
            townHall.assignPosition(self)
        for hut in huts:
            if not hut.isDestroyed:
                hut.assignPosition(self)
        for wall in walls:
            if not wall.isDestroyed:
                wall.assignPosition(self)
        for cannon in cannons:
            if not cannon.isDestroyed:
                cannon.assignPosition(self)
        for tower in towers:
            if not tower.isDestroyed:
                tower.assignPosition(self)
        if not mainKing.isDead:
            mainKing.updatePosition(self)
        if not mainQueen.isDead:
            mainQueen.updatePosition(self)
        for barbarian in arraybarbarians:
            if not barbarian.isDead:
                barbarian.updatePosition(self)
                barbarian.changeColor(self)
        for archer in arrayArchers:
            if not archer.isDead:
                archer.updatePosition(self)
                archer.changeColor(self)
        for balloon in arrayBalloons:
            if not balloon.isDead:
                balloon.updatePosition(self)
                balloon.changeColor(self)
        self.drawMap()