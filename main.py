import numpy as np
import colorama as cm

class building:
    isDestroyed = False
    currHealth = None
    
    def __init__(self, x, y, w, h, hitpoints):
        self.startingX = x
        self.startingY = y
        self.sizeX = w
        self.sizeY = h
        self.hitpoints = hitpoints
        self.currHealth = hitpoints

# Each building below shows inheritance
class cannon(building): 
    def __init__(self, x, y, w, h, damage, range):
        super().__init__(x, y, w, h)
        self.damage = damage
        self. range = range

class wall(building):
    def __init__(self, x, y, w, h, hitpoints):
        super().__init__(x, y, w, h, hitpoints) # w and h should both be 1

class hut(building):
    def __init__(self, x, y, w, h, hitpoints):
        super().__init__(x, y, w, h, hitpoints)

class townHall(building):
    def __init__(self, x, y, w, h, hitpoints):
        super().__init__(x, y, w, h, hitpoints) ## w=4 and h=3 

class spawningPoint:
    def __init__(self, x, y):
        self.positionX = x
        self.positionY = y

class movingObject:
    isdead = False
    currPositionX = None
    currPositionY = None
    currHealth = None
    fullhealth = None

    def __init__(self, startX, startY, health, speed, damage):
        self.startPositionX = startX
        self.startPositionY = startY
        self.currHealth = health
        self.hitpoints = health
        self.movSpeed = speed
        self.damage = damage

class king(movingObject): 
    def __init__(self, startX, startY, health, speed, damage):
        super().__init__(startX, startY, health, speed, damage)
    def move(self, pressedKey):
        if pressedKey == "w":
            self.currPositionY -= 1
        elif pressedKey == "a":
            self.currPositionX += 1
        elif pressedKey == "d":
            self.currPositionX -= 1
        elif pressedKey == "s":
            self.currPositionY += 1

class barabarian(movingObject):
    def __init__(self, startX, startY, health, speed, damage):
        super().__init__(startX, startY, health, speed, damage)
    


        
