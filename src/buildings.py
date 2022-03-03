from map import *

class building:
    isDestroyed = False
    currHealth = None
    
    def __init__(self, x, y, hitpoints):
        self.positionX = x
        self.positionY = y
        self.fullHealth = hitpoints
        self.currHealth = hitpoints

    def assignHeight(self, h):
        self.height = h
    
    def assignmaxWidth(self, w):
        self.maxWidth = w
    
    def assignTexture(self, texture):
        self.texture = texture

    def assignInitialPosition(self, mainMap):
        for i in range(mainMap.verticalBoundary + self.positionY, self.height + mainMap.verticalBoundary + self.positionY):
            for j in range(mainMap.horizontalBoundary + self.positionX, len(self.texture[i - mainMap.verticalBoundary - self.positionY]) + mainMap.horizontalBoundary + self.positionX):
                if self.texture[i-mainMap.verticalBoundary - self.positionY][j-mainMap.horizontalBoundary - self.positionX] != "\n":
                    mainMap.grid[i][j] = self.texture[i-mainMap.verticalBoundary - self.positionY][j-mainMap.horizontalBoundary - self.positionX]
                    mainMap.grid[i][j] = Fore.BLACK + Back.GREEN + mainMap.grid[i][j] 
            

# Each building below shows inheritance
class cannon(building): 
    def __init__(self, x, y, damage, range):
        super().__init__(x, y)
        self.damage = damage
        self. range = range

class wall(building):
    def __init__(self, x, y, hitpoints):
        super().__init__(x, y, hitpoints) # w and h should both be 1

class hut(building):
    def __init__(self, x, y, hitpoints):
        super().__init__(x, y, hitpoints)

class townHall(building):
    def __init__(self, x, y, hitpoints):
        super().__init__(x, y, hitpoints) ## w=4 and h=3 