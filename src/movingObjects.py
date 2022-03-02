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
