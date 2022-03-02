import numpy as np
import colorama
from colorama import Fore, Back

class map:
    grid = []

    def __init__(self, rows, cols, x , y):
        self.rows = rows
        self.cols = cols
        self.origX = x
        self.origY = y
    
    def make_canvas(self):
        self.grid = []
        for r in range(self.rows + self.origY):
            row = []
            if r < self.origY:
                for c in range(self.cols + self.origX):
                    row.append(Back.RESET + " ")
            else:
                for c in range(self.cols + self.origX):
                    if c < self.origX:
                        row.append(Back.RESET + " ")
                    else:
                        if r == self.origY or r == self.origY + self.rows -1 or  c == self.origX + self.cols -1 or c == self.origX:
                            row.append(Back.WHITE + Fore.WHITE + " ")
                        else:
                            row.append(Back.BLACK + Fore.BLACK + " ")
            
            self.grid.append(row)
            
    # print everything
    def draw_canvas(self):
        canvas_str = ""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                canvas_str += self.grid[r][c]
            
            canvas_str += '\n'    

        print('\033[H' + canvas_str)

