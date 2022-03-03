import numpy as np
import colorama
from colorama import Fore, Back

class map:
    grid = []
    
    def __init__(self, rows, cols, x , y, h, v):
        self.rows = rows
        self.cols = cols
        self.originateX = x
        self.originateY = y
        self.horizontalBoundary = h
        self.verticalBoundary = v
    
    def createMap(self):
        for i in range(self.originateY, self.originateY + 2 * self.verticalBoundary + self.rows):
            row = []
            if i < self.originateY + self.verticalBoundary:
                for j in range(self.originateX, self.originateX + 2 * self.horizontalBoundary + self.cols): 
                    row.append(Back.YELLOW + " ")
            elif i >= self.originateY + self.verticalBoundary + self.rows:
                for j in range(self.originateX, self.originateX + 2 * self.horizontalBoundary + self.cols):
                    row.append(Back.YELLOW + " ")
            else:
                for j in range(self.originateX, self.originateX + 2 * self.horizontalBoundary + self.cols):
                    if j < self.originateX + self.horizontalBoundary or j >= self.originateX + self.horizontalBoundary + self.cols:
                        row.append(Back.YELLOW + " ")
                    else:
                        row.append(Back.GREEN + " ")
            self.grid.append(row)
            
    def drawMap(self):
        printMap = ""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                printMap += self.grid[r][c]
            printMap += '\n'    
        print('\033[H' + printMap)

