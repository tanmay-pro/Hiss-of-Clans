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