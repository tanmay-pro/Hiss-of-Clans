import numpy as np
import colorama
from colorama import Fore, Back

class map:
    grid = []

    def __init__(self, rows, cols, x , y):
        self.rows = rows
        self.cols = cols
        self.originateX = x
        self.originateY = y
    
    def createMap(self):
        for i in range(self.originateY -1, self.rows + self.originateX + 1):
            row = []
            if i == self.originateY - 1 or i == self.originateX + self.rows:
                for j in range(self.originateX - 2, self.cols + self.originateY + 2):
                    row.append(Back.YELLOW + " ")
            else:
                for j in range(self.originateX - 2, self.cols + self.originateY + 2):
                    if j == self.originateX -2 or j == self.originateX -1 or j == self.cols + self.originateY + 1 or j == self.cols + self.originateY:
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

