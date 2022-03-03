import numpy as np
import colorama
from colorama import Fore, Back

class map:
    grid = []
    
    def __init__(self, cols, rows, h, v):
        self.rows = rows
        self.cols = cols
        self.horizontalBoundary = h
        self.verticalBoundary = v
    
    def createMap(self):
        for i in range(0, 2 * self.verticalBoundary + self.rows):
            row = []
            if i < 0 + self.verticalBoundary:
                for j in range(0, 2 * self.horizontalBoundary + self.cols): 
                    row.append(Back.YELLOW + Fore.YELLOW +" ")
            elif i >= 0 + self.verticalBoundary + self.rows:
                for j in range(0, 2 * self.horizontalBoundary + self.cols):
                    row.append(Back.YELLOW + Fore.YELLOW + " ")
            else:
                for j in range(0, 2 * self.horizontalBoundary + self.cols):
                    if j < 0 + self.horizontalBoundary or j >= 0 + self.horizontalBoundary + self.cols:
                        row.append(Back.YELLOW + Fore.YELLOW + " ")
                    else:
                        row.append(Back.GREEN + Fore.GREEN + " ")
            self.grid.append(row)
            
    def drawMap(self):
        printMap = ""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                printMap += self.grid[r][c]
            printMap += '\n'    
        print('\033[H' + printMap)

